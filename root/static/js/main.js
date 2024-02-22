async function getResearch() {
    const response_promise = await fetch("/beheerder/dashboard");
    const anwser = await response_promise.json();
    console.log(anwser)
}