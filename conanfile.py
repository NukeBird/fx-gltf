from conans import ConanFile, CMake

class FxGltfConan(ConanFile):
    name = "fx-gltf"
    version = "1.1.0"
    license = "MIT"
    url = "https://github.com/NukeBird/fx-gltf"
    description = "A C++14/C++17 header-only library for simple, efficient, and robust serialization/deserialization of glTF 2.0"
    exports = "*"
    build_policy = "missing"

    def package(self):
       self.copy("*.h", dst="include", src="include")
