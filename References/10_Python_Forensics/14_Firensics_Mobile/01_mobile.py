


"""

Python Forensics - Mobile Forensics

Forensic investigation and analysis of standard computer hardware such as hard disks have developed into a stable discipline and is followed with the help of techniques to analyze non-standard hardware or transient evidence.

Although smartphones are increasingly being used in digital investigations, they are still considered as non-standard.

Forensic Analysis
Forensic investigations search for data such as received calls or dialed numbers from the smartphone. It can include text messages, photos, or any other incriminating evidence. Most smartphones have screen-locking features using passwords or alphanumeric characters.

Here, we will take an example to show how Python can help crack the screen-locking password to retrieve data from a smartphone.

Manual Examination
Android supports password lock with PIN number or alphanumeric password. The limit of both passphrases are required to be between 4 and 16 digits or characters. The password of a smartphone is stored in the Android system in a special file called password.key in /data/system.

Android stores a salted SHA1-hashsum and MD5-hashsum of the password. These passwords can be processed in the following code.

It is not feasible to crack the password with the help of dictionary attack as the hashed password is stored in a salt file. This salt is a string of hexadecimal representation of a random integer of 64 bit. It is easy to access the salt by using Rooted Smartphone or JTAG Adapter.

Rooted Smartphone
The dump of the file /data/system/password.key is stored in SQLite database under the lockscreen.password_salt key. Under settings.db, the password is stored and the value is clearly visible in the following screenshot.

Rooted Smartphone
JTAG Adapter
A special hardware known as JTAG (Joint Test Action Group) adapter can be used to access the salt. Similarly, a Riff-Box or a JIG-Adapter can also be used for the same functionality.

Using the information obtained from Riff-box, we can find the position of the encrypted data, i.e., the salt. Following are the rules −

Search for the associated string "lockscreen.password_salt."

The byte represents the actual width of the salt, which is its length.

This is the length which is actually searched for to get the stored password/pin of the smartphones.

These set of rules help in getting the appropriate salt data.


"""

public byte[] passwordToHash(String password) {

   if (password == null) { 
      return null; 
   }

   String algo = null;
   byte[] hashed = null;

   try { 
      byte[] saltedPassword = (password + getSalt()).getBytes(); 
      byte[] sha1 = MessageDigest.getInstance(algo = "SHA-1").digest(saltedPassword);
      byte[] md5 = MessageDigest.getInstance(algo = "MD5").digest(saltedPassword); 
      hashed = (toHex(sha1) + toHex(md5)).getBytes(); 
   } catch (NoSuchAlgorithmException e) { 
      Log.w(TAG, "Failed to encode string because of missing algorithm: " + algo); 
   }
   
   return hashed;
}



