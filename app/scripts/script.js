async function askQuestion() {
    const question = document.getElementById("question").value;
    const responseBox = document.getElementById("response");

    responseBox.innerHTML = "Loading ...";

    const res = await fetch("/ask", {
        method: "POST",
        headers: {"Content-Type": "applications/json"},
        body: JSON.stringify({question})
    });

    const data = await res.json();
    responseBox.innerHTML = data.answer || "No answer returned.";
}