var filename="/Resources/2018-07-21 13-30-56.txt";
var reader=new FileReader();
reader.readAsText(filename);
reader.onload=function(ev){
    alert("hello");
    var p=document.createElement('p')
    p.innerHTML=reader.result;
    document.body.appendChild(p);
}
document.write('<img src="./pic.png">');
