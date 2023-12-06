const sendToArticles = (key, value) => {
    let url = window.location.href.split('?')[0];
    let search = window.location.search;
    const hasArticles = url.includes('articles');
    if (!hasArticles) {
        url += 'articles/';
        search = '?page=1&paginate_by=10';
    }

    const urlParams = new URLSearchParams(search);

    urlParams.set(key, value);

    window.location.href = url + '?' + urlParams.toString();
}

function redirectToArticle(articleId) {
    const url = window.location.href.split('/')[0];
    window.location.href = `${url}/articles/` + articleId + '/';
}

const categorySideNav = document.getElementsByClassName('categorySideNav');

for (let category of categorySideNav) {
    category.addEventListener('click', function () {
        sendToArticles('category', category.innerText)
    })
}


const button = document.getElementById('header-button');
const sidenav = document.getElementById('custom-sidenav');
const backdrop = document.getElementById('sidenavBackgrop');

button.addEventListener('click', () => {
    sidenav.classList.toggle('custom-sidenav--closed');
    backdrop.classList.toggle('sidenavBackgrop--closed');
});

backdrop.addEventListener('click', () => {
    sidenav.classList.toggle('custom-sidenav--closed');
    backdrop.classList.toggle('sidenavBackgrop--closed');
});

const searchButton = document.getElementById('searchButton');
const searchInput = document.getElementById('searchInput');

searchButton.addEventListener('click', () => {
    sendToArticles('search', searchInput.value);
});

const cleanFilters = document.getElementById('cleanFilters');
cleanFilters.addEventListener('click', () => {
    const url = window.location.href

    window.location.href = url.split('?')[0];
});
const paginateSelect = document.getElementById('paginateSelect');

paginateSelect.addEventListener('change', () => {
    sendToArticles('paginate_by', paginateSelect.value);
})