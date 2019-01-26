from conans import ConanFile, CMake
from conans import tools
from conans.tools import os_info, SystemPackageTool
import os, sys
import sysconfig
from io import StringIO

class RosbagConan(ConanFile):
    name = "rs_bag2image"
    version = "0.1.3"

    description = "rs_bag2image"
    url = "https://github.com/ulricheck/rs_bag2image.git"
    license = "GPL"

    short_paths = True
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "virtualrunenv"

    requires = (
        "opencv/[>=3.4.0]@camposs/stable",
        "librealsense/2.17.1@camposs/stable",
		"glew/2.1.0@camposs/stable",
        "glext/1.3@camposs/stable",
       )

    default_options = (
    	"opencv:shared=True",
    	"librealsense:shared=True",
    )

    # all sources are deployed with the package
    exports_sources = "*.cpp", "*.h", "CMakeLists.txt"

    def imports(self):
        self.copy(src="bin", pattern="*.dll", dst="./bin") # Copies all dll files from packages bin folder to my "bin" folder
        self.copy(src="lib", pattern="*.dll", dst="./bin") # Copies all dll files from packages bin folder to my "bin" folder
        self.copy(src="lib", pattern="*.dylib*", dst="./lib") # Copies all dylib files from packages lib folder to my "lib" folder
        self.copy(src="lib", pattern="*.so*", dst="./lib") # Copies all so files from packages lib folder to my "lib" folder
        self.copy(src="bin", pattern="ut*", dst="./bin") # Copies all applications
        self.copy(src="bin", pattern="log4cpp.conf", dst="./") # copy a logging config template
        self.copy(src="share/Ubitrack", pattern="*.*", dst="./share/Ubitrack") # copy all shared ubitrack files 
       
    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure()
        cmake.build()
        cmake.install()
