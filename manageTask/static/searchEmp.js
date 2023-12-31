// searching Employee section using tree
const btn = document.getElementById('searchEmployee')
const btn_name = document.getElementById('search_name_employee')
btn.onclick = () => {
    const searched = document.getElementById('search').value
    const sr = {'search': searched, 'key': 'salary'}
    fetch('/task/search-employee/', {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(sr)
    }).then(res => {
        return res.json();
    }).then(data => {
        console.log(data);
    });
}
btn_name.onclick = () => {
    const searched = document.getElementById('search_name').value
    const sr = {'search': searched, 'key': 'username'}
    fetch('/task/search-employee/', {
        method: 'POST',
        headers: {
            'content-type': 'application/json'
        },
        body: JSON.stringify(sr)
    }).then(res => {
        return res.json();
    }).then(data => {
        console.log(data);
    });
}