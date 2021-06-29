#!/usr/bin/python3 


import cgi
import subprocess as sb

print("content-type: text/html")
print()

print('''<style>
pre{
    color: black;
    font-weight: bold;
    font-size: 25px;
    
}
</style>''')


fs = cgi.FieldStorage()

cmd = fs.getvalue("commands")
name = fs.getvalue("name") 
replica = fs.getvalue("replica")
deployment= fs.getvalue("deployment")
image= fs.getvalue("image")
port = fs.getvalue("port")

#cmd = input("enter req...")
#name = input("pod name : ")
#replica = input("replica : ")
#port = input("port : ")

if("all" in cmd ) and ("pods" in cmd):
    output = sb.getoutput("kubectl get pods --kubeconfig admin.conf")    
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")
    
elif("all" in cmd) and ("deployments" in cmd):
    output = sb.getoutput("kubectl get deployment --kubeconfig admin.conf")
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")


elif(("create" in cmd) or ("launch" in cmd ) and ("pod" in cmd ):
    output = sb.getoutput("kubectl run {} --image=centos:latest --kubeconfig admin.conf".format(name))
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")


elif("deployment" in cmd) and ("create" in cmd ):
    output = sb.getoutput("kubectl create deployment {} --image=centos:latest --kubeconfig admin.conf ".format(name))
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")


elif("deployment" in cmd) and ("expose") and ("port number"):
    output = sb.getoutput("kubectl expose deployment {} --port={} --type=NodePort --kubeconfig admin.conf ".format(name,port))
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")


elif("create" in cmd ) or ("scale" in cmd ) and (("replica" in cmd ) or ("deployment" in cmd )):
    output = sb.getoutput("kubectl scale deployment  {} --replicas={} --kubeconfig admin.conf ".format(name,replica))
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")


elif ("delete" in cmd ) and ("pod" in cmd):
    output = sb.getoutput("kubectl delete pods {} --kubeconfig admin.conf".format(name))
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")


elif("delete" in cmd ) and ("deployment" in cmd ):
    output = sb.getoutput("kubectl delete deployment {}  --kubeconfig admin.conf" .format(name))
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("<pre>{}</pre>".format(output))
    print("</body>")


else:
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("<pre>Invelid Input...</pre>")
    print("</body>")