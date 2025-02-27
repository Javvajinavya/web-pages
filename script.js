function checkSyntax() {
    let code = document.getElementById("codeInput").value;
    let language = document.getElementById("language").value;
    let output = document.getElementById("output");

    fetch("http://localhost:5000/check-syntax", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ language, code }),
    })
    .then(response => response.json())
    .then(data => {
        output.textContent = data.result;
        output.style.color = data.error ? "red" : "green";
    })
    .catch(error => {
        output.textContent = "Error connecting to server!";
        output.style.color = "red";
    });
}

function logout() {
    localStorage.removeItem("loggedInUser");
    window.location.href = "index.html";
}
