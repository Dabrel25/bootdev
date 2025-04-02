import * as cowsay from "cowsay"
import {moo} from "./moo.js";

console.log(cowsay.say({
    text: moo("Bob"),
}));

    