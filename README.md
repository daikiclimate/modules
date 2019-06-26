# Upload modules for practice

Just I made a module that sending Log of deep learning to my email address when learning finished.

clone repo and make available for python

```
git clone git@github.com:daikiclimate/modules.git
python setup.py develop
```

second you should change Datorch/mailog.py to input your mailaddress and something

```
vi Datorch/mailog.py
```

and change below

```mailog.py
   #settings
    to_email = "aaaa@gmail.com"
    from_email = "bbbb@gmail.com"

    gmail_account = "aaaa@gmail.com"
    gmail_password = "cccc"
```

It's finished settings.

In your leaning code, you add these modules

```
import Datorch.mailog as mailog
```

and add this end of code

```
mailog.sendmail("Sending Log!","log.txt")
```

It is nessesary that your logs are saved in log.txt
Maybe It's better to use printfunc.py together.

pringfunc.py provide you to print log or write csvfile. It can help you make code smart

This is add just like this

```
from Datorch.printlog import Logfunc
Logf = Logfunc()

for epoch in range(10):
    ...
    ...
    Logf.update(epoch, train_loss, test_loss)
    Logf.print_log()
    Logf.write_log()

```

Logf makes log.txt and help mailog send massage
