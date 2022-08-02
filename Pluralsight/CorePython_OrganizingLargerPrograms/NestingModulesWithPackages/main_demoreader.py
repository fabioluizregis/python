import demo_reader
import demo_reader.multireader
import demo_reader.compressed

print(type(demo_reader))
print(demo_reader.__file__)


r = demo_reader.multireader.MultiReader('demo_reader/__init__.py')
print(r.read())
r.close()

print(demo_reader.compressed.__file__)