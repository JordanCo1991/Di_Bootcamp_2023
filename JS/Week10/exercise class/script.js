
const{ userInfo } = require('./userinfo.js')

userInfo().then ((data)=> {
    console.log(data);
});