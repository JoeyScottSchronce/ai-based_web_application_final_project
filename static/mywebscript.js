let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    if (!textToAnalyze.trim()) {
        document.getElementById("system_response").innerHTML = "Please enter some text for analysis.";
        return;  // Stop if no text is provided
    }

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze" + "=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
}