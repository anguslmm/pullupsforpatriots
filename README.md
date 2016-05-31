```
 ___      _ _   _   _            __           ___      _       _     _      
| _ \_  _| | | | | | |_ __ ___  / _|___ _ _  | _ \__ _| |_ _ _(_)___| |_ ___
|  _/ || | | | | |_| | '_ (_-< |  _/ _ \ '_| |  _/ _` |  _| '_| / _ \  _(_-<
|_|  \_,_|_|_|  \___/| .__/__/ |_| \___/_|   |_| \__,_|\__|_| |_\___/\__/__/
                     |_|                                                    
```
Ascii art made [here](http://patorjk.com/software/taag/#p=display&f=Small&t=Pull%20Ups%20for%20Patriots).

This is the main repository for the [PullUpsForPatriots website](http://www.pullupsforpatriots.com "Pull Ups for Patriots").

## Purpose

This website is made to collect donations for the Company D Marines at Fort
Gordon for the [Hope for the Warriors](http://www.hopeforthewarriors.org) Charity organization.

## Getting Started for Developers

For the guys working on this project, create a new workspace in cloud9, 
preferably named `pullupsforpatriots`. Then you'll need to set up the
environment and clone the git repository.

### Setting Up Your Environment.

#### Switching from Python 2 to 3

At the command line in
cloud9, first delete the `python` alias, then create a new one to `python3`.

```
$ sudo ln -sfn /usr/bin/python3 /usr/bin/python
```
Alternatively, if that didn't work:
```
$ sudo rm /usr/bin/python
$ sudo ln -s /usr/bin/python3 /usr/bin/python
```
Then check to make sure it worked:
```
$ python --version
Python 3.4.3
```

#### Getting the Newest Django

Now that we have Python 3 as our default, we need to make sure we have the right
verison of Django. Thankfully, there is a python package manager called `pip` 
that will do that for us.

```
$ sudo pip install -U Django
```

The `-U` flag makes sure that, if we already have Django, it will update to the
newest version. Now let's make sure we have the right version.

```
$ python -c "import django; print(django.get_version())"
1.9.6
```

### Getting Started With Git 

Hopefully by this point I've showed you the basics of git already. Now it's time
to try them out in the real world!

I've created a git repository on github, but obviously you know that, because
you're looking at the readme!

First you'll need to make an account with GitHub (I know, you're sick of making
acounts, I'm sure.)

Clear all the files out of your cloud9 workspace so that they only folder is the
single root `pullupsforpatriots` folder. Then it's time to clone the repository.

We could use SSH instead of HTTPS, but HTTPS is much easier to get started with
since it doesn't require us to deal with public and private keys.
```
$ git clone https://github.com/anguslmm/pullupsforpatriots.git
```
If at any point git asks you to authenticate, it will be your user name and
password from github.

#### Making and Pushing Your First Git Commit

First things first, we want to create our own branch. You should never be
working directly on the master branch.

```
$ git checkout -b angus-branch
```
This command both creates and checks out a new branch called `angus-branch`. 
Obviously, you should name your branch with your name.

Now for the changes you're making in your branch. Open this README.md in your
locally cloned copy of the repository (inside cloud9), and add a message with 
your name inside the quoted block below.
```
What's up! -Angus
How's it going? -Ruiz
```
Save the file, then close it. Now we're going to see one of the main functions
of branches: that they track changes seperately. First we need to commit our
changes to the branch.
```
git commit -am "Add my message"
```
This adds a commit with our changes to the branch, with the commit message
`Add my message`. The `-a` flage means we're adding all changes that we've made,
and the `-m` flag means we're setting our commit message in the quotes that
follow. It's important that commit messages are in the impertive tense. So our 
message says `Add my message`, not `Adding my message` or `Added my message`. 

Now check out the master branch, and you'll see that your message doesn't appear
in the README.md anymore.
```
$ git checkout master
```
But we saved our changes, so where did they go? You just switched your local
repository to show you the master branch, which hasn't been changed since we
cloned the repository. Now switch back to your branch...
```
$ git checkout angus-branch
```
...and you'll see that your message is back.

But how do you get your changes added to that master branch? No one else will 
see them and they won't affect the website as it is launched until you do. So
first we need to push your branch to the "origin", or the main git repository on
GitHub.
```
$ git push origin angus-branch
```
If you get tired of typing branch names, remember that the tab key will
autocomplete stuff for you.

Great! So now our branch is on the remote (origin) repository, but still aren't
part of the master branch. This is where GitHub helps us our. Go to the
repository page on GitHub, and create a "pull request". This is a request for me
to "pull" the changes in your branch into the master branch. Once you have all
done this, I'll pull them changes you've all made in, and all your messages will
appear in the copy of this README.md that appears on the github site.

This process is how you'll make changes to the code, then submit them.

#### Git Tips
* Commit often. If you can think of a commit message for your changes, commit.
* Push to the remote repository before you leave your workstation. That way your changes are accesible from anywhere and never lost.
* Remember to make commit messages imperative statements, and short but descriptive.
* Don't make pull requests until you've tested your code and it works.
* There are tons of Git cheatsheets online. Use them! And I'm always available too.
* Be on the lookout: I'll be using the "Issues" function on GitHub to assign tasks to you!