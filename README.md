
# FinalProjectJCDS
<b> Final Project JCDS Purwadhika </b><br>
<u>Predicting the success and failure of campaigns on Kickstarter</u>

dataset:  https://www.kaggle.com/kemical/kickstarter-projects


this project is made as my Final Project on Purwadhika's Data Science and Machine Learning Job Connector Program
there are several limitations on this project
1. this could only predict the success and failure of the campaign. success on the campaign does not mean the campaigner will actually deliver the product
2. this is a two-week project, so this project is still in it's experimental stage

on this project, I will be using Logistic Regression because it turned out to be the one that returns the lowest false positive rate.
<b>1. Dataset</b>
![Capture](https://user-images.githubusercontent.com/64766681/92573715-602dc680-f2b0-11ea-9036-0e6006d9d822.JPG)

<u>name</u>						: the name column is basically the name of the campaign. will be dropped later on.
<u>category</u>				: the subcategory of the campaign
<u>main_category</u>		: the main category of the campaign
<u>currency</u>				: the currency based on the origin of the campaign
<u>deadline</u>				: the end of the campaign time, set by the campaigner
<u>goal</u>						: the goal of the campaign, in local currency
<u>launched</u>				: the time of the campaign started going live
<u>pledged</u>				: the final recorded amount of money pledged, in local currency
<u>backers</u>					: the final recorded number of backers
<u>country</u>					: the campaign's country of origin
<u>usd pledged</u>		: the final recorded amount of money pledged, in USD, converted manually
<u>usd_pledged_real</u>		: the final recorded amount of money pledged, in USD, converted using fixer.io API
<u>usd_goal_real</u>		: the goal of the campaign, in USD

<b> Dropped Columns </b>
*DROPPING 'usd pledged'*

description in kaggle:  

-   usd pledged = Pledged amount in USD (conversion made by KS)  
    
-   usd_pledged_real = Pledged amount in USD (conversion made by fixer.io api)

usd pleged is more problematic than usd_pledged_real with the same intentions

*DROPPING 'pledged'*

'pledged' is still using local currency. since we're going to use usd_pledged_real, we'll be dropping pledged

*DROPPING 'goal'*

-   goal is the actual goal with locale currency. to keep everything in sync, we'll be using everything converted to USD in the usd_goal_real columns

*DROPPING 'currency'*

-   currency explains nothing more than country of the origin of the project. since everything is converted to USD, currency is no longer relevant
- 
<b>*CONVERTED 'values'*</b>
*not including Live and Canceled*

Live and Cancelled are 2 states that we're not going to include LIVE = is currently asking for pledges and backers and haven't meet their deadline yet. so it is not considered either successful or failed. canceled is a state where the campaign was canceled by the campaigners due to errors, mistakes in the campaign, and various other reasons

*merging suspended and undefined*

suspended means the campaign is being "locked" by Kickstarter due to several problems and probably due to the campaigner's violate Kickstarter's Terms and Conditions

however, the state undefined is unclear. there is no information on what is undefined. because investors or backers only want successful campaigns, undefined is stated as failed

*unifying Dates in 'launched" and 'deadline'* 
convert to datetime and remove the timestamp, plus adding a new feature to calculate total dates available between launched and deadline



























<br><br><br><br><br><br><br><br>
EXTERNAL NOTE:
this project is under Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
because I'm using https://www.kaggle.com/kemical/kickstarter-projects which also uses (CC BY-NC-SA 4.0) license

You are free to:
Share — copy and redistribute the material in any medium or format
Adapt — remix, transform, and build upon the material

Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

NonCommercial — You may not use the material for commercial purposes.

ShareAlike — If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

https://creativecommons.org/licenses/by-nc-sa/4.0/ for more information




