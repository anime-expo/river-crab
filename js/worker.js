import python from "https://shift.js.org/wasm/python.js";
import makeConfig from "https://shift.js.org/wasm/common.js";

async function load(url) {
    const response = await fetch(url);
    return await response.text();
}

self.addEventListener('message', async (ev) => {
    const script = await load(ev.data.script);
    const input = ev.data.input;
    const fn = (text) => self.postMessage(text);
    python(makeConfig(script, fn, input));
})