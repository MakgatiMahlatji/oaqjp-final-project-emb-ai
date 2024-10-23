let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("POST", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    xhttp.setRequestHeader("Content-Type", "application/json"); // Set the content type
    xhttp.send(JSON.stringify({ text: textToAnalyze }));
}
