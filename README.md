## Login System

### How it works

**Registration**<br>
There will be an Input which will be encoded in sha256.
Then the username and the sha256 hash will be set into the `db.json` file.
After that the username will be set into the `usernames` Array. _(For a easier username check)_

**Login**<br>
First it checks if the username is in the `usernames` Array.
If there is not the username, then it will check the password.
The password will be encoded to a sha256 hash and that will be checked with the hash in the json.
If the hash is correct it will be login you.

### Why i did that?
Idk... i was bored.
