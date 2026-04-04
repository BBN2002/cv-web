// Glow effect following the cursor
const cursorGlow = document.querySelector('.cursor-glow');

document.addEventListener('mousemove', (e) => {
    cursorGlow.style.left = e.clientX + 'px';
    cursorGlow.style.top = e.clientY + 'px';
});

// Typewriter effect
const nameElement = document.querySelector('.typewriter-xinrui');
const textToType = "BEINING";
let i = 0;

function typeWriter() {
    if (i < textToType.length) {
        nameElement.innerHTML += textToType.charAt(i);
        i++;
        setTimeout(typeWriter, 150);
    } else {
        nameElement.innerHTML += '<span class="cursor"></span>';
    }
}

// Reveal elements on scroll
function reveal() {
    var reveals = document.querySelectorAll(".reveal");
    for (var i = 0; i < reveals.length; i++) {
        var windowHeight = window.innerHeight;
        var elementTop = reveals[i].getBoundingClientRect().top;
        var elementVisible = 150;
        if (elementTop < windowHeight - elementVisible) {
            reveals[i].classList.add("active");
        }
    }
}

window.addEventListener("scroll", reveal);

// Navbar background change on scroll
window.addEventListener('scroll', () => {
    const nav = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        nav.classList.add('scrolled');
    } else {
        nav.classList.remove('scrolled');
    }
});

// Initialize
window.addEventListener('load', () => {
    setTimeout(typeWriter, 500);
    reveal(); // Trigger once on load
});
