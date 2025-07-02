async function askQuestion() {
    const question = document.getElementById("question").value;
    const responseBox = document.getElementById("response");

    
    console.log("Question entered:", question); 
    
    responseBox.innerHTML = "Thinking ...";

    try {
        const res = await fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({question})
        });

        if (!res.ok) {
            const errorText = await res.text();
            console.error("❌ Server error:", errorText);
            responseBox.innerHTML = "Server error: " + errorText;
            return;
        }

        const data = await res.json();
        responseBox.innerHTML = data.answer || "No answer returned.";
    } catch (error) {
        console.error("Error calling API:", error);
        responseBox.innerHTML = "An error occurred while fetching the answer.";
    }
}