from conans import ConanFile, tools, AutoToolsBuildEnvironment


class Liburing(ConanFile):
    name = "liburing"
    version = "2.0"
    license = "LGPL and MIT"
    author = "Pavel Davydov pdavydov108@gmail.com"
    url = "https://github.com/axboe/liburing"
    description = "Conan package for liburing."
    settings = "os", "compiler", "arch"
    generators = "make"

    @property
    def source_dir(self):
        return f'liburing-liburing-{self.version}/'


    def source(self):
        if self.settings.os == "Linux":
            package_url = f'{self.url}/archive/refs/tags/liburing-{self.version}.tar.gz'
            tools.get(package_url)

    def build(self):
        if self.settings.os == "Linux":
            with tools.chdir(self.source_dir):
                autobuild = AutoToolsBuildEnvironment(self)
                autobuild.configure()
                autobuild.make()

    def package(self):
        if self.settings.os == "Linux":
            self.copy("*.h", dst="include", src=self.source_dir)
            self.copy("*.a", dst="lib", src=self.source_dir, keep_path=False)

    def package_info(self):
        if self.settings.os == "Linux":
            self.cpp_info.libs = ["liburing"]

