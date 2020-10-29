const tableContainer = document.querySelector('.table-container')
const schema = {
    name: 'Name',
    username: 'Username',
    email: 'E-mail',
    website: 'Website'
}

xhr = new XMLHttpRequest()
xhr.open('GET', 'https://jsonplaceholder.typicode.com/users')

xhr.send()

xhr.addEventListener('load', getUsers)

function getUsers () {
    const [...users] = JSON.parse(xhr.responseText)
    renderUsers(users)
}

function renderUsers (users) {
    console.log(users)
    let fragment = document.createDocumentFragment()
    let thead = generateTr(schema, schema, 'th') //document.createElement('thead')
    let tbody = document.createElement('tbody')
    for (let user of users) {
        tbody.appendChild(generateTr(schema, user))
    }

    fragment.append(thead)
    fragment.append(tbody)
    tableContainer.appendChild(fragment)
    console.log(tableContainer)
}

function generateTr (schema, item, tag='tr') {
    let tr = tag === 'tr' ? document.createElement(tag) : document.createElement('thead')
    for (let k of Object.keys(schema)) {
        if (k in item) {
            let td = document.createElement(tag === 'tr' ? 'td' : tag)
            td.textContent = item[k]
            if (k === 'name') {
                td.addEventListener('click', (event) => alert(`Name: ${item.name}, UserName: ${item.username}`))
            }
            tr.appendChild(td)
        }
    }

    return tr
}

// document.body.innerHTML = new_str