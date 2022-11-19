from cProfile import label
import csv
import random
from statistics import mean
import sys
import time
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3
from numpy.linalg import norm


def usage():
    """ print usage of the program"""
    print("USAGE: Kmeans.py [FILEPATH] [NCENTROID] [MAX_ITER]")
    print("\tPATH:      The absolute path to the data CSV file.")
    print("\tNCENTROID: Number of Centroids.")
    print("\tMAX_ITER:  Maximum number of iterations.")
    quit()

def dist_euclid(a, b, norme = 1):
    """returns the Euclidean distance between two points a and b
        with coordinates in the form of numpy.array: [x,y,z,...]

        args:
            a & b are ndArray with shape  = n * 1
            norme: type of the norme to calculate :
                The L1 norm that is calculated as the sum of the 
                    absolute values of the vector. 

                The L2 norm that is calculated as the square root
                    of the sum of the squared vector values (dist euclidienne)
        return:
            float        
    """
    if norme == 1:   #norme L1
        return abs(np.sum(a - b))
    else:   # Norme L2
        return np.sqrt(np.sum(np.square(a - b)))
    

def ft_progress(lst):
    """prompt the lst with EAT"""
    i = 1
    start = time.time()
    while i <= len(lst):
        yield i
        pourc = int(i * 100 / len (lst))
        nb = int(i * 20 / len(lst))
        arrow = ">".rjust(nb, "=")
        top = time.time() - start
        eta = (len(lst) * top / i) - top
        print(f"ETA: {eta:.2f}s [{pourc:3}%] [{arrow:<20}] {i}/{len(lst)} | elapsed time {top:.2f}s", end = '\r', flush=True)
        i += 1
    print("")


class CsvReader():
    def __init__(self, filename=None, sep=',', header=False):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.header_fields = None

        try:
            self.file = open(self.filename,'rt', newline='')
        except FileNotFoundError as e:
            print(f"{filename} not found")
            self.file = None

    def __enter__(self):
        if self.file != None:
            read = csv.reader(self.file, delimiter=self.sep, quotechar='\"', quoting=csv.QUOTE_NONE)
            self.data = list(read)
            if self.header:
                self.header_fields = self.data[0]
            self.nb_value = len(self.data[0])
            return self
        return None

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file != None:
            self.file.close()


    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:  nested list (list(list, list, ...)) representing the data.
        """
        if self.header:
            return self.data[1:]
        else:
            return self.data

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        return self.header_fields

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids
        self.std = False
        self.walks = []
        self.norme_dist = 1         #L1 ou L2

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
            None.
        Raises:
        -------
            This function should not raise any Exception.
        """
        list_of_centroids_array = []
        list_of_centroids_walks = []
        if self.std:
            self.standartisation()
        for i in ft_progress(range(self.max_iter)):
            self.centroids = self.random_cluster(X)
            
            old_centroids_list = self.centroids
            convergence = False
            # walks = []            #remove comment to save only best walks
            while not convergence:
                clusters = self.assign_to_cluster()
                self.centroids = self.find_centroids(clusters)
                convergence = True if np.sum(old_centroids_list - self.centroids) == 0 else False
                self.walks.append(self.centroids)
                old_centroids_list = self.centroids
            #congergence -> stock le resultat avec la somme des dist
            sum = self.sum_dist_all_point()
            list_of_centroids_array.append([self.centroids, sum])
            # list_of_centroids_walks.append(walks) #remove comment to save only best walks
        best_sum = list_of_centroids_array[0][1]
        for idx, centre in enumerate(list_of_centroids_array[1:]):
            s = centre[1] # sum of dist of this centroid
            if s < best_sum:
                best_sum = s
                self.centroids = centre[0]
                # self.walks = list_of_centroids_walks[idx] #remove comment to save only best walks
            
    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
            X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
            the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
            This function should not raise any Exception.
        """
        result = []
        for point in X:
            min_dist = 100000000.0
            nearest_centroid = -1
            for num_centroid, centroid in enumerate(self.centroids):
                dist = dist_euclid(point, centroid, self.norme_dist)
                if dist < min_dist:
                    min_dist = dist
                    nearest_centroid = num_centroid
            if nearest_centroid != -1:
                result.append(nearest_centroid)
        return result

    def load(self, path):
        """load the file in path and return np.array of the data"""
        with CsvReader(path,',', True) as file:
            if file:
                data_brut = np.array(file.getdata(), dtype=float)
                self.header = np.array(file.getheader(), dtype=str)
                nb_data = len(data_brut)
                print(f"loading {nb_data} data(s) ...ok")
                self.data = data_brut[:,(1,2,3)] # remove first col
                return self.data
            else:
                return None

    def random_cluster(self, array):
        """
            return a list of nb_cluster random cluster
        """
        cluster_list = np.zeros((self.ncentroid, array.shape[1]), dtype=float) #shape(3, nb_cluster)
        nb = len(array)
        i = 0
        while i < self.ncentroid:
            c = array[random.randint(0, nb - 1)]
            if c not in cluster_list:
                cluster_list[i] = c
                i += 1
        return cluster_list

    def set_standart_on(self):
        """put the flag on to standartization"""
        self.std = True

    def set_standart_off(self):
        """put the flag off to standartization"""
        self.std = False

    def standartisation(self):
        """ standartisation of data"""
        print("Standardisation... ", end="")
        mean = np.mean(self.data[:,2], axis=0) #only  the bone_density
        std = np.std(self.data[:,2], axis=0)
        self.data[:,2] = (self.data[:,2] - mean) / std
        minimum = np.min(self.data[:,2])
        if minimum < 0:
            self.data[:,2] = self.data[:,2] - minimum
        print("OK")

    def assign_to_cluster(self):
        """
            returns a array of distribution of points in clusters

            return:
                clusters of centroids
        """
        resultat = self.predict(self.data)
        clusters = []
        
        for i in range(self.ncentroid):
            clusters.append([self.data[idx] for idx, nb_centroid in enumerate(resultat) if nb_centroid == i])
        return np.array(clusters, dtype=object)

    def find_centroids(self, clusters):
        """
            Args:
                clusters: array of K clusters containing the related points 
            return:
                centroids: list
        """
        centroid = []
        for cluster in clusters:
            centroid.append(np.mean(cluster, axis=0))
        return np.array(centroid)

    def sum_dist_all_point(self):
        """return the sum of all dist between points and centroids of clusters"""
        sum = 0
        clusters = self.assign_to_cluster()
        for idx, cluster in enumerate(clusters):
            centre = self.centroids[idx]
            for point in cluster:
                sum += dist_euclid(point, centre, self.norme_dist)
        return sum


def show_table(array, header):
    print(" #  ", end="")
    for h in header:
        print(f"{h: ^15}", end =" ")
    print("\n-------------------------------------------------")
    for idx, ligne in enumerate(array):
        print(f"{idx: ^3}", end=" ")
        if isinstance(ligne, np.ndarray):
            for data in ligne:
                print(f"{data: >14.10f}", end=" ")
            print("\n")
        else:
            print(f"{ligne: ^15}")
    print("-------------------------------------------------")
    print(f"nb data = {len(array)}")

def graph3d(kmeans):
    """ plot 3D graph"""
    D = pd.DataFrame(data, columns=kmeans.header[1:])
    resu = kmeans.predict(data)
    label_ = []
    colors = np.array(["blue","green","red","black"])
    for x in resu:
        if x == beld_citizens:
            label_.append("Beld")
        elif x == mars_citizen:
            label_.append("Mars")
        elif x == venus_citizen:
            label_.append("Venus")
        else:
            label_.append("Earth")
    if len(label_) > 0:
        D['labels'] = label_
    df = pd.DataFrame({"x" : data[:,0], "y" : data[:,1], "z" : data[:,2]})
    fig = plt.figure(figsize=(12, 20))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title('Solar System_census')
    ax.set_xlabel('Height')
    ax.set_ylabel('Weight')
    ax.set_zlabel('Bone density')
    ax.scatter(D.height, D.weight, D.bone_density, c=colors[resu], s=10, label=label_)
    if len(kmeans.centroids) > 0:
        for idx, centre in enumerate(kmeans.centroids):
            ax.scatter(centre[0], centre[1], centre[2], c=colors[idx], s=40, marker="X")
            ax.text(centre[0], centre[1], centre[2], '%s' % (label_[idx]), size=10, c=colors[idx])

def graph2D(kmeans):
    """ plot 2d Analyse graph"""
    D = pd.DataFrame(data, columns=kmeans.header[1:])
        
    resu = kmeans.predict(data)
    label_ = []
    for x in resu:
        if x == beld_citizens:
            label_.append("Beld")
        elif x == mars_citizen:
            label_.append("Mars")
        elif x == venus_citizen:
            label_.append("Venus")
        else:
            label_.append("Earth")
    D['labels'] = label_

    sns.pairplot(D, hue="labels")

def animate_scatters(iteration, data, scatters):
    """
    Update the data held by the scatter plot and therefore animates it.
    Args:
        iteration (int): Current iteration of the animation
        data (list): List of the data positions at each iteration.
        scatters (list): List of all the scatters (One per element)
    Returns:
        list: List of scatters (One per element) with new coordinates
    """
    for i in range(data[0].shape[0]):
        scatters[i]._offsets3d = (data[iteration][i,0:1], data[iteration][i,1:2], data[iteration][i,2:])
        ax.set_title('Solar System_census : ' + str(iteration)+"/"+str(iterations))
    return scatters


if __name__ == "__main__":
    """Main entry"""
    if (len(sys.argv)) != 4:
        usage()
    #control args
    if isinstance(sys.argv[1], str):
        try:
            path=sys.argv[1]
            ncentroid = int(sys.argv[2])
            max_iter = int(sys.argv[3])
        except Exception:
            usage()
    else:
        usage()
    kmeans = KmeansClustering(ncentroid = ncentroid, max_iter=max_iter)
    kmeans.norme_dist = 2
    kmeans.set_standart_off()
    data = kmeans.load(path)
    if data is not None:

        kmeans.fit(data)
        
        mean_tab = []
        clusters = kmeans.assign_to_cluster()
        print("\n#     height     weight       bone_density      Nb")
        for idx, cluster in enumerate(clusters):
            height_mean = np.mean(cluster[idx][0])
            weight_mean = np.mean(cluster[idx][1])
            bones_mean = np.mean(cluster[idx][2])
            mean_tab.append([idx, height_mean, weight_mean, bones_mean])
            print(f"{idx: <2} : {height_mean: >8.4f}\t{weight_mean: >8.4f}\t{bones_mean: >7.4f}\t\t{len(cluster): <3}")
        ###### Found Citizens #####
        #Beld Citizens
        mean_tab = np.array(mean_tab)
        mean_tab = mean_tab[mean_tab[:, 3].argsort()]   #sort by bone_density

        beld_citizens = int(mean_tab[0][0])     # the first is the lowest bone_density
        print(f"Lowest bone_density is cluster #{beld_citizens} -> Citizens of the Belt")
        mean_tab = np.delete(mean_tab, (0), axis=0)

        #Mars
        mean_tab = mean_tab[mean_tab[:, 1].argsort()]   #sort by height
        mars_citizen = int(mean_tab[-1][0])             #the last is the tallest mean
        print(f"Tallest mean is on cluster {mars_citizen} --> mars")
        mean_tab = np.delete(mean_tab, (-1), axis=0)
        
        #Venus
        mean_tab = mean_tab[mean_tab[:, 2].argsort()]   #sort by weight
        venus_citizen = int(mean_tab[0][0])             #the first is the slender mean
        print(f"Slender mean on cluster {venus_citizen} --> venus")
        print(f"The earth's Citizens of Earth is {int(mean_tab[1][0])}")
        if len(kmeans.walks)> 0:

            fig = plt.figure(figsize=(12, 20))
            ax = fig.add_subplot(111, projection='3d')
            
            ax.set_xlabel('Height')
            ax.set_ylabel('Weight')
            ax.set_zlabel('Bone density')
            # Initialize scatters
            D = pd.DataFrame(data, columns=kmeans.header[1:])
            # scatters = [ ax.scatter(kmeans.walks[0][i,0:1], kmeans.walks[0][i,1:2], kmeans.walks[0][i,2:], marker="x") for i in range(kmeans.walks[0].shape[0]) ]
            
            resu = kmeans.predict(data)
            label_ = []
            c = np.array(["blue","green","red","black"])
            colors = np.array([c[resu[0]],c[resu[1]], c[resu[2]], c[resu[3]]])

            for x in resu:
                if x == beld_citizens:
                    label_.append("Beld")
                elif x == mars_citizen:
                    label_.append("Mars")
                elif x == venus_citizen:
                    label_.append("Venus")
                else:
                    label_.append("Earth")
            iterations = len(kmeans.walks)              # Number of iterations
            if iterations > 0:
                D['labels'] = label_
                scatters = []
                scatters = [ ax.scatter(kmeans.walks[0][i,0:1], kmeans.walks[0][i,1:2], kmeans.walks[0][i,2:], marker="x", c=colors[i], s=40,) for i in range(kmeans.walks[0].shape[0]) ]
                scatters.append(ax.scatter(D.height, D.weight, D.bone_density, c=c[resu], s=10, label=label_))
                ax.set_title('Solar System_census : 0/'+str(iterations))
            
            ani = animation.FuncAnimation(fig, animate_scatters, iterations, fargs=(kmeans.walks, scatters),
                                        interval=150, blit=False, repeat=False)
        graph2D(kmeans)
        graph3d(kmeans)
        plt.show()
    quit()
