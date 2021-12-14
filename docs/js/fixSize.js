var width = window.innerWidth
    || document.documentElement.clientWidth
    || document.body.clientWidth;

if (width <= 1000){
    document.body.classList
        .remove("big")
    document.body.classList
        .add("small")
}