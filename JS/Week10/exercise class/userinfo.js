const userInfo = async() => {
    try{
        const res = await fetch('https://jsonplaceholder.typicode.com/users');
        const data= await res.json();
        return data;
    } catch (err) {
        console.log(err);
    }
}

module.exports = {
    userInfo,

}