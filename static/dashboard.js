
// javascript code for changing the focus relating to the nav link

const anchorLinks = document.querySelectorAll('.link');
console.log(anchorLinks);

anchorLinks.forEach(link => {
  link.addEventListener('click', event => {
    //event.preventDefault();
    const activeLinks = document.querySelector('.link.active');
    console.log(activeLinks);
    if (activeLinks) {
      activeLinks.classList.remove('active');
    }
     event.currentTarget.classList.add('active');
  });
});

