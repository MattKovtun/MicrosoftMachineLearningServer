## Example of Microsoft Machine Learning Server usage, which shows how to deploy trained model and then use it<br>
#### In order to be able to test Microsoft Machine Learning Server (MMLS) first of all you should install it<br>
https://docs.microsoft.com/en-us/machine-learning-server/install/machine-learning-server-windows-install<br>
Don't forget to deploy it, also remember credentials.<br>
`az ml admin bootstrap`<br>
#### Next step <br>
Install keras and tensorflow to `conda`, which is inside of MMLS or you can use `pip`. In my case it was:<br>
`pip3 install --upgrade tensorflow`<br>
`conda install -c conda-forge keras`<br>
#### Next is model.<br>
You can download models from [model folder](./model), or you can train a new model.
#### MMLS communcation.<br>
Generally we can deploy some functionality for further usage, later destroy.<br>
In [main file](./MMLS_example.py) you will see authentication process and 3 functions: <b>deploy, explore, destroy</b>.<br>
#### Connection<br>
Put your login and password here. You got those after setting up MMLS. <br>
`context = (login, password)`<br>
#### Usage <br>
Now simply run <b>deploy -> explore -> destroy</b>.<br>
Don't be afraid of warnings and errors, MMLS produces a lot of them. :)<br>
If everything is fine the output should be simmilar to this: <br>
`{'answer': 3}`<br><br>
### Enjoy!
