import { spawn } from "child_process";

import FileSystem from "../Modules/FileSystem.js";
import * as Config from "../Config/index.js";

class Search {
    path = FileSystem.GetPath(Config.Search.container, Config.Search.file_init, Config.Search.extension);

    // interval = 30000 - 1000;

    Run() {
        // setInterval(() => {
        //     const child = spawn("python", [this.path]);
        //     child.stdout.on("data", (data) => {
        //         console.log(String(data));
        //     });
        // }, this.interval);
    }
}

export default new Search();
