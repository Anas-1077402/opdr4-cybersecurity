async function getDashboardData() {
    const response_promise = await fetch("/beheerder/dashboard/all");
    const anwser = await response_promise.json();
    document.getElementById('research').innerHTML = anwser['research'];
    document.getElementById('experience_expert').innerHTML = anwser['experience_expert'];
    console.log(anwser)
}

window.addEventListener('load', function() {
    if (document.getElementById('research')) {
        getDashboardData();
        setInterval(getDashboardData, 1000)
    }
});
