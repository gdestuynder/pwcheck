# pwcheck
Just a password checker

Looks like that (success):

```
~/git/pwcheck (master) ⚡ ./pwcheck.py thisisagood
Checking your password is within acceptable range of the ideal entropy (80% close to ideal target entropy)
You password has 2.9139770731827523 entropy for a length of 11 - ideal entropy is 3.4594316186372978 and you're close enough ( above 2.7675452949098385).
Searching for commonly used passwords...: 14310941it [00:25, 561856.11it/s]
Success! This password look potentially like a good one for it's length.
```

And that (entropy failure):

```
~/git/pwcheck (master) ⚡ ./pwcheck.py thisisagoodpassword
Checking your password is within acceptable range of the ideal entropy (80% close to ideal target entropy)
Your password is not safe, please choose a safer password. Your entropy 3.2608281712244565, target entropy 3.3983420107548685.
```

Or that (common/known password failure):

```
~/git/pwcheck (master) ⚡ ./pwcheck.py 218CAB9M3
Checking your password is within acceptable range of the ideal entropy (80% close to ideal target entropy)
You password has 3.169925001442312 entropy for a length of 9 - ideal entropy is 3.1699250014423126 and you're close enough ( above 2.53594000115385).
Searching for commonly used passwords...: 1284657it [00:02, 563522.76it/s]You password is a commonly used password, that's not safe.
```
