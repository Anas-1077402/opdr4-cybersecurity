

async function getResearchStatus() {
    const response_promise = await fetch("/beheerder/dashboard");
    const anwser = await response_promise.json();
    console.log(response_promise)
    console.log(anwser)
}

window.addEventListener('load', function() {
    if (document.getElementsByClassName('btn btn-primary 1')) {
        getResearchStatus();
        setInterval(getResearchStatus, 1000)
    }
});
