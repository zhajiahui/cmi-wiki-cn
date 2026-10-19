# LobFile Hosting

**Recommended.**

**Warning**

File size limit is 100MB for this hosting method. Higher limits are available with a LobFile subscription.

Automatically upload your resourcepack on a **free online service** with servers all over the world.\
Thanks a lot to [LobFile](https://lobfile.com/), which provides us their platform to host files for free!


## What are the advantages?

* Download speed.
* Availability.
* Security: Your server IP address is not exposed.
* No high bandwidth usage.

## I already use `self-host`, is this better?

Depends.

It's better to use [self-host](/plugin-usage/plugin-configuration/resourcepack-hosting/self-hosting.md) if you're working on the resourcepack and you have to continuously run `/iazip`, to avoid losing time (read more [here](/plugin-usage/beginners/fast-resourcepack-tips.md)).

When you've finished working on the pack you can safely start using this other hosting feature instead of `self-host`, in this case **LobFile**.\
This will make your server traffic lower as the resourcepack won't be hosted on your server anymore.\
If your playerbase is all from the same country, you can stick with `self-host`.

## Setup

#### Step 1

Create an account on [LobFile here](https://lobfile.com/sign-up).

#### Step 2

Open your [account settings](https://lobfile.com/dashboard/general) and enable _**"Continuous Uploading"**_

<figure><img src="../../../.gitbook/assets/lobfile_003.png" alt=""><figcaption></figcaption></figure>

#### Step 3

On the [Account Info](https://lobfile.com/dashboard/account-info) dashboard, click on your API key to copy it to your clipboard.

<figure><img src="../../../.gitbook/assets/lobfile_002.png" alt=""><figcaption></figcaption></figure>

#### Step 4

Enable `lobfile` in `config.yml` and disable all the other hosting methods.

```yaml
lobfile:
  enabled: true
```

Open `secret.yml` and paste your `API Key`.

```yaml
lobfile:
  api_key: xxxxxxxxxx
```

#### Step 5

Run `/iazip.`

Wait for the Privacy policy message to appear.\
Run `/acceptprivacy` to accept the policy (will be asked only the first time).

### Done

The **plugin** will **upload it** online **automatically**.\
Nothing else to do, enjoy your **free automated resourcepack hosting**.

## Will my resourcepack be available online to random people?

2023-12-21:\
Your resourcepack won't be indexed on Google and won't be published in a list of resourcepacks.\
Only people who know the link can download the pack.

I take no responsibility, the product is provided as is and I am not the owner of LobFile.
