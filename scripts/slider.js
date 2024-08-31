function sliderLoad() {
    let items = document.querySelectorAll('.fourthSectionContainer .sectionFourthSlider .slider .item')
    let active = 3;
    function loadShow() {
        items.forEach((item, index) => {
            item.style.transform = 'none';
            item.style.zIndex = 2;
            item.style.filter = 'none';
            item.style.opacity = 1;

            if (index === active) {
                item.style.transform = 'none';
                item.style.zIndex = 2;
                item.style.filter = 'none';
                item.style.opacity = 1;
            } else if (index === active - 1 && active > 0) {
                let stt = 1;
                item.style.transform = `translateX(${-120 * stt}px) scale(${1 - 0.2 * stt}) perspective(16px) rotateY(1deg)`;
                item.style.zIndex = stt;
                item.style.filter = 'blur(5px)';
                item.style.opacity = stt > 2 ? 0 : 0.6;
            } else if (index === active + 1 && active < items.length - 1) {
                let stt = 1;
                item.style.transform = `translateX(${120 * stt}px) scale(${1 - 0.2 * stt}) perspective(16px) rotateY(-1deg)`;
                item.style.zIndex = stt;
                item.style.filter = 'blur(5px)';
                item.style.opacity = stt > 2 ? 0 : 0.6;
            } else {
                item.style.transform = 'none';
                item.style.zIndex = 0;
                item.style.filter = 'none';
                item.style.opacity = 0;
            }
        });
    }
    loadShow();
    let next = document.getElementById('next');
    let prev = document.getElementById('prev');
    next.onclick = function () {
        active = active + 1 < items.length ? active + 1 : active;
        loadShow();
    }
    prev.onclick = function () {
        active = active - 1 >= 0 ? active - 1 : active;
        loadShow();
    }
    if (items.length > 0) {
        return true
    } else {
        return false
    }
   }
   
sliderLoad();