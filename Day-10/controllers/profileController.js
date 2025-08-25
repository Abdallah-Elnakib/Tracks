const profile = (req,res) =>{
    res.render('profile',{username : 'abdallah', age : 27,
         phone: '1258777',role : 'user'})
}


module.exports = {profile}


