async function getResearchStatus() {
    const response_promise = await fetch("/beheerder/dashboard/all");
    const anwser = await response_promise.json();
    document.getElementById('research').innerHTML = anwser['research'];
}

window.addEventListener('load', function() {
    if (document.getElementById('research')) {
        getResearchStatus();
        setInterval(getResearchStatus, 1000)
    }
});
