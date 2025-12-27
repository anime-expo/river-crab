const worker = new Worker("/js/worker.js", {type: 'module'});

export async function invoke(script, input) {
    return new Promise((resolve) => {
        worker.postMessage({script, input});
        worker.onmessage = (ev) => resolve(ev.data);
    });
}

async function encrypt() {
    const inputText = document.getElementById("input").value;
    const outputText = await invoke("/python/encrypt.py", inputText);
    document.getElementById("output").value = outputText;
}

async function decrypt() {
    const inputText = document.getElementById("input").value;
    const outputText = await invoke("/python/decrypt.py", inputText);
    document.getElementById("output").value = outputText;
}

document.getElementById("encrypt").addEventListener("click", encrypt);
document.getElementById("decrypt").addEventListener("click", decrypt);
