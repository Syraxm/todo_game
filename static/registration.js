// todo: input validation
async function create_new_user(){
    var name = document.getElementById('user_name').value
    var apiUrl = `http://127.0.0.1:5000/register?u_name=${name}`

    const response = await fetch(apiUrl)
    if (response.ok)
    {
        open('http://127.0.0.1:5000/')
    }
    else
    {
        alert('try again')
    }
}
