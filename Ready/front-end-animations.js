document.addEventListener('DOMContentLoaded', function() {
    const topics = document.querySelectorAll('.topic');
    const progressBar = document.getElementById('progress-bar');

    topics.forEach(topic => {
        topic.addEventListener('click', function() {
            const target = this.getAttribute('id');
            const targetElement = document.getElementById(target);

            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });

    document.addEventListener('scroll', function() {
        const scrollDistance = window.scrollY;
        const windowHeight = window.innerHeight;
        const fullHeight = document.body.clientHeight;

        const progress = (scrollDistance / (fullHeight - windowHeight)) * 100;
        progressBar.style.width = progress + '%';
    });
});
