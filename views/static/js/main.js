(function () {

    const selecionar = (el, all = false) => {
        el = el.trim()
        if (all) {
            return [...document.querySelectorAll(el)]
        } else {
            return document.querySelector(el)
        }
    }

    const ligado = (type, el, listener, all = false) => {
        let selectEl = selecionar(el, all)
        if (selectEl) {
            if (all) {
                selectEl.forEach(e => e.addEventListener(type, listener))
            } else {
                selectEl.addEventListener(type, listener)
            }
        }
    }

    const rolagem = (el, listener) => {
        el.addEventListener('scroll', listener)
    }

    // aciona o navbar ao fazer a rolagem de tela

    let linksMenu = selecionar('#navbar .scrollto', true)
    const linksAtivos = () => {
        let position = window.scrollY + 200
        linksMenu.forEach(navbarlink => {
            if (!navbarlink.hash) return
            let section = selecionar(navbarlink.hash)
            if (!section) return
            if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
                navbarlink.classList.add('active')
            } else {
                navbarlink.classList.remove('active')
            }
        })
    }
    window.addEventListener('load', linksAtivos)
    rolagem(document, linksAtivos)

    // Vai até a posição do link clicado no navbar

    const rolarPara = (el) => {
        let elementPos = selecionar(el).offsetTop
        window.scrollTo({
            top: elementPos,
            behavior: 'smooth'
        })
    }

    // navbar mobile

    ligado('click', '.mobile-nav-toggle', function (e) {
        selecionar('body').classList.toggle('mobile-nav-active')
        this.classList.toggle('bi-list')
        this.classList.toggle('bi-x')
    })

    // Não muda o link na barra de navegão ao utilizar o nav-menu

    ligado('click', '.scrollto', function (e) {
        if (selecionar(this.hash)) {
            e.preventDefault()

            let body = selecionar('body')
            if (body.classList.contains('mobile-nav-active')) {
                body.classList.remove('mobile-nav-active')
                let navbarToggle = selecionar('.mobile-nav-toggle')
                navbarToggle.classList.toggle('bi-list')
                navbarToggle.classList.toggle('bi-x')
            }
            rolarPara(this.hash)
        }
    }, true)

    // animação da página inicial

    const typed = selecionar('.typed')
    if (typed) {
        let typed_strings = typed.getAttribute('data-typed-items')
        typed_strings = typed_strings.split(',')
        new Typed('.typed', {
            strings: typed_strings,
            loop: true,
            typeSpeed: 100,
            backSpeed: 50,
            backDelay: 2000
        });
    }

    // Animação de rolagem de tela

    window.addEventListener('load', () => {
        AOS.init({
            duration: 1000,
            easing: '',
            once: true,
            mirror: false
        })
    });


})()