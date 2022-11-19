pip install --upgrade pip
pip install virtualenv
python3 -m pip install --upgrade build
PYTHON_VERSION=$(ls $VIRTUAL_ENV/lib)
mkdir $VIRTUAL_ENV/lib/$PYTHON_VERSION/site-packages/my_minipack
python -m build
