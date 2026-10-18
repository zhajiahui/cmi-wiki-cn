# Quest Status Fact

The `QuestStatusFact` is a fact that returns the status of a specific quest.

This fact can only be **read**, not written to. Hence, it is only suitable for criteria.

| Status | Value |
| --- | --- |
| Inactive | 0 |
| Active | 1 |
| Active and Tracked | 2 |
| Completed | -1 |

**warning**

The **completed** status has a value of **-1**, this is to make it easy to query if the quest is active by `>= 1`.

## How could this be used? {#how-could-this-be-used}

This can be used to abstract the status of a quest.
If a quest has multiple criteria, you can check for this fact instead of checking for each criterion.

## Fields {#fields}

## Comment

Inherited Optional

A comment to keep track of what this fact is used for.

## Group

Required

## Quest

Required
