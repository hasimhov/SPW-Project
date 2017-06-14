var a=0,b=0,c=0,d=0,e=0,f=0,first=0,password;
var sub=document.getElementById("submit");
function emailcheck() 
{
    var x = document.getElementById("email");
    var x1=document.getElementById("email1");
    var atpos = x.value.indexOf("@");
    var dotpos = x.value.lastIndexOf(".");
    if (atpos<1 || dotpos<atpos+2 || dotpos+2>=x.length) 
    {
        x1.innerHTML="Invalid Email ID";
        x.style.borderColor="red";
        a=0;
    }
    else
    {
        x1.innerHTML="";
        x.style.borderColor="green";
        a=1;   
        if(a==1&&b==1&&c==1&&d==1&&e==1&&f==1)
            sub.disabled=false;
    }
}
function namecheck() 
{
    var x = document.getElementById("name");
    var x1=document.getElementById("name1");
    var exp = new RegExp("^[a-zA-Z\ ]{3,}$");
  var te=exp.test(x.value);
    if (x.value.length==0) 
    {
        x1.innerHTML="Name cannot be empty";
        x.style.borderColor="red";
        d=0;
    }
    else if (!te) {
        x1.innerHTML="Give your Real Name & no special Characters";
        x.style.borderColor="red";
        d=0;      
    }

    else
    {
        x1.innerHTML="";
        x.style.borderColor="green";
        d=1;
        if(a==1&&b==1&&c==1&&d==1&&e==1&&f==1)
            sub.disabled=false;   
    }
}
function bdatecheck(){
var d=/^(((19|20)([2468][048]|[13579][26]|0[48])|2000)[/-]02[/-]29|((19|20)[0-9]{2}[/-](0[4678]|1[02])[/-](0[1-9]|[12][0-9]|30)|(19|20)[0-9]{2}[/-](0[1359]|11)[/-](0[1-9]|[12][0-9]|3[01])|(19|20)[0-9]{2}[/-]02[/-](0[1-9]|1[0-9]|2[0-8])))$/;
  var x=document.getElementById("bdate");
    var x1=document.getElementById("bdate1");
    var isnum = d.test(x.value);
    if(isnum==true&&x.value.length==10)
    {
        x.style.borderColor="green";
        x1.innerHTML="";
        e=1;
        if(a==1&&b==1&&c==1&&d==1&&e==1&&f==1)
            sub.disabled=false;
    }
    else
    {
        x1.innerHTML="Wrong Date .Check Format";
        x.style.borderColor="red";
        e=0;
    }
}
function phonecheck()
{
    var x=document.getElementById("phoneno");
    var x1=document.getElementById("phoneno1");
    var isnum = /^\d+$/.test(x.value);
    if(isnum==true&&x.value.length==10)
    {
        x.style.borderColor="green";
        x1.innerHTML="";
        f=1;
        if(a==1&&b==1&&c==1&&d==1&&e==1&&f==1)
            sub.disabled=false;
    }
    else
    {
        x1.innerHTML="Phone no should consist of exactly 10 digits";
        x.style.borderColor="red";
        f=0;
    }
}

function pwdcheck()
{
  var x=document.getElementById("pwd");
    var x1=document.getElementById("pwd1");
    password = x.value;
    //Password should contain atleast one alphabet, atleast one numeric character, atleast one special character and password length should be atleast 6
    var exp = new RegExp("^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{6,})");
  var te=exp.test(password);
    if(te==false) 
  {
      x1.innerHTML="Password should contain atleast one number one special character and at least 6 characters";
        x.style.borderColor="red";
        b=0;    
    }
    else
    {
        x1.innerHTML="";
        x.style.borderColor="green";
        b=1;
        if(a==1&&b==1&&c==1&&d==1&&e==1&&f==1)
            sub.disabled=false;   
    }
    if(first!=0)
        conpwdcheck();
    else
        first=1;
}

function conpwdcheck()
{ var x = document.getElementById("conpwd");
    var x1=document.getElementById("conpwd1");
  if(x.value===password&&b==1)
  {
        x1.innerHTML="";
        x.style.borderColor="green";
        c=1;
        if(a==1&&b==1&&c==1&&d==1&&e==1&&f==1)
            sub.disabled=false;   
    }
    else
    {
        x1.innerHTML="Passwords do not match";
        x.style.borderColor="red";
        c=0;
    }
}

function submit()
{   
    if(a==0||b==0||c==0||d==0||e==0||f==0)
    {
         sub.disabled=true;
         emailcheck();
         namecheck();
         phonecheck();
         pwdcheck();
         conpwdcheck();
         bdatecheck();
    }
}
function submit1()
{
    var form = document.getElementById("signupform");
    var elements = form.elements;
    var len = elements.length
    for (var i = 0; i < len; ++i) 
    {
        elements[i].readOnly = true;
    }
    document.getElementById("state").disabled=true;
    sub.disabled=true;
    alert("Submitted Successfully");
}

