import { resolve } from "path";

class FileSystem {
    root = process.cwd();

    containers = "App/Containers";

    GetPath(directory, file_init, extension) {
        const path = resolve(this.root, this.containers, directory, file_init + "." + extension);
        return path;
    }
}

export default new FileSystem();
