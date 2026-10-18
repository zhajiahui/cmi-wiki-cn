# Basic Adapter

The Basic Adapter contains all the essential entries for Typewriter.
In most cases, it should be installed with Typewriter.
If you haven't installed Typewriter or the adapter yet,
please follow the [Installation Guide](https://docs.typewritermc.com/docs/getting-started/installation)
first.

## Entries {#entries}

### Actions {#actions}

| Name | Description |
| --- | --- |
| [Add Potion Effect Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/add_potion_effect) | Add a potion effect to the player |
| [Apply Velocity Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/apply_velocity) | Apply a velocity to the player |
| [Cinematic](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/cinematic) | Start a new cinematic |
| [Console Command Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/console_run_command) | Run command from console |
| [Delayed Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/delayed_action) | Delay an action for a certain amount of time |
| [Drop Item Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/drop_item) | Drop an item at location, or on player |
| [Firework Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/firework) | Spawns a firework |
| [Give Item Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/give_item) | Give an item to the player |
| [Group Trigger Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/group_trigger_action) | Trigger the next entries for everyone in the same group as the player |
| [Message Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/send_message) | Send a message to a player |
| [Play Sound Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/play_sound) | Play sound at player, or location |
| [Player Command Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/player_run_command) | Make player run command |
| [Random Trigger Gate](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/random_trigger) | Randomly selects its connected triggers |
| [Remove Item Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/remove_item) | Remove an item from the players inventory |
| [Set Block Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/set_block) | Set a block at a location |
| [Set Item Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/set_item) | Set an item in a specific slot |
| [Show Title Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/show_title) | Show a title to a player |
| [Simple Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/simple_action) | Simple action to modify facts |
| [Spawn Particle Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/spawn_particles) | Spawn particles at location |
| [Stop Sound Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/stop_sound) | Stop a or all sounds for a player |
| [Switch Server Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/switch_server_action) | Switches the player to another server |
| [Teleport Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/teleport) | Teleport a player |
| [Track Quest Action](https://docs.typewritermc.com/adapters/BasicAdapter/entries/action/track_quest) | Start tracking a quest for a player |

### Audiences {#audiences}

| Name | Description |
| --- | --- |
| [Boss Bar](https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/boss_bar) | Boss Bar |
| [Cinematic Audience](https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/cinematic_audience) | Filters an audience based on if they are in a cinematic |
| [Closest Group Member Path Stream](https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/closest_group_member_path_stream) | A Path Stream to the Closest Group Member |
| [Criteria Audience](https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/criteria_audience) | An audience filter based on criteria |
| [Cron Audience](https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/cron_audience) | Filters an audience based if the time matches a cron expression |
| [Direct Location Path Stream](https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/direct_location_path_stream) | A Path Stream to a Direct Location |
| [Game Time Audience](https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/game_time_audience) | Filters an audience based on the game time |
| [Group Members Path Stream](https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/group_members_path_stream) | A Path Stream to Group Members |
| [Holding Item Audience](https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/holding_item_audience) | Filters an audience based on if they are holding a specific item |
| [Item In Inventory Audience](https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/item_in_inventory_audience) | Filters an audience based on if they have a specific item in their inventory |
| [Item In Slot Audience](https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/item_in_slot_audience) | Filters an audience based on if they have a specific item in a specific slot |
| [Location Objectives Path Stream](https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/location_objectives_path_stream) | A Path Stream to tracked Location Objectives |
| [Looping Cinematic Audience](https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/looping_cinematic_audience) | Show the audience members a cinematic that loops |
| [Simple Lines](https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/simple_lines) | Statically determined lines of text |
| [Simple Sidebar](https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/sidebar) | Display a sidebar for players |
| [Tab List Header Footer](https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/tab_list_header_footer) | Set the header and footer of the tab list |
| [Timer Audience](https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/timer_audience) | Triggers an action every specified duration when the player is in the audience |
| [Trigger Audience](https://docs.typewritermc.com/adapters/BasicAdapter/entries/audience/trigger_audience) | Triggers a sequence when the player enters or exits the audience |

### Cinematics {#cinematics}

| Name | Description |
| --- | --- |
| [Action Bar Dialogue Cinematic](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/actionbar_dialogue_cinematic) | Show an action bar typed dialogue |
| [Blinding Cinematic](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/blinding_cinematic) | Blind the player so the screen looks black |
| [Camera Cinematic](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/camera_cinematic) | Create a cinematic camera path |
| [Cinematic Console Command](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/cinematic_console_command) | Runs command as the console at a specific frame. |
| [Cinematic Player Command](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/cinematic_player_command) | Runs command as the player at a specific frame. |
| [Particle Cinematic](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/particle_cinematic) | Spawn particles for a cinematic |
| [Potion Effect Cinematic](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/potion_effect_cinematic) | Apply different potion effects to the player during a cinematic |
| [Pumpkin Hat Cinematic](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/pumpkin_hat_cinematic) | Show a pumpkin hat during a cinematic |
| [Random Action Bar Dialogue Cinematic](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/random_actionbar_dialogue_cinematic) | Show a random action bar typed dialogue |
| [Random Spoken Dialogue Cinematic](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/random_spoken_dialogue_cinematic) | Play a random spoken dialogue cinematic |
| [Random Subtitle Dialogue Cinematic](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/random_subtitle_dialogue_cinematic) | Show a random action bar message |
| [Screen Shake Cinematic](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/screen_shake_cinematic) | Shake the screen |
| [Set Fake Block Cinematic](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/set_fake_block_cinematic) | Set a fake block |
| [Sound Cinematic](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/sound_cinematic) | Play a sound during a cinematic |
| [Spoken Dialogue Cinematic](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/spoken_dialogue_cinematic) | Play a spoken dialogue cinematic |
| [Subtitle Dialogue Cinematic](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/subtitle_dialogue_cinematic) | Show an subtitle message |
| [Title Cinematic](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/title_cinematic) | Show a title during a cinematic |
| [Trigger Sequence Cinematic](https://docs.typewritermc.com/adapters/BasicAdapter/entries/cinematic/trigger_sequence_cinematic) | A sequence of triggers to run |

### Dialogues {#dialogues}

| Name | Description |
| --- | --- |
| [Message Dialogue](https://docs.typewritermc.com/adapters/BasicAdapter/entries/dialogue/message) | Display a single message to the player |
| [Option Dialogue](https://docs.typewritermc.com/adapters/BasicAdapter/entries/dialogue/option) | Display a list of options to the player |
| [Random Message Dialogue](https://docs.typewritermc.com/adapters/BasicAdapter/entries/dialogue/random_message) | Display a random message from a list to a player |
| [Random Spoken Dialogue](https://docs.typewritermc.com/adapters/BasicAdapter/entries/dialogue/random_spoken) | Display a random selected animated message to the player |
| [Spoken Dialogue](https://docs.typewritermc.com/adapters/BasicAdapter/entries/dialogue/spoken) | Display a animated message to the player |

### Events {#events}

| Name | Description |
| --- | --- |
| [Block Break Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_block_break) | When the player breaks a block |
| [Block Place Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_place_block) | When the player places a block |
| [Chat Contains Text Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_message_contains_text) | When the player sends a chat message containing certain text |
| [Craft Item Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/craft_item_event) | Called when a player crafts an item |
| [Detect Command Ran Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_detect_command_ran) | When a player runs an existing command |
| [Fire Trigger Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/fire_trigger_event) | Trigger the event when a player runs `/tw fire <entry id/name> [player]` |
| [Fish Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_fish) | When the a player caught a fish or an item |
| [Interact Block Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_interact_with_block) | When the player interacts with a block |
| [Pickup Item Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_item_pickup) | When the player picks up an item |
| [Player Death Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_player_death) | When a player dies |
| [Player Hit Entity Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_player_hit_entity) | When a player hits an entity |
| [Player Join Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_player_join) | When the player joins the server |
| [Player Kill Entity Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_player_kill_entity) | When a player kills an entity |
| [Player Kill Player Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_player_kill_player) | When a player kills a player |
| [Player Near Location Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_player_near_location) | When the player is near a certain location |
| [Player Quit Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_player_quit) | When the player quits the server |
| [Run Command Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/event/on_run_command) | When a player runs a custom command |

### Facts {#facts}

| Name | Description |
| --- | --- |
| [Countdown Fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/countdown_fact) | A fact that counts down from the set value |
| [Cron Fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/cron_fact) | Saved until a specified date, like (0 0 * * 1 |
| [In Audience Fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/in_audience_fact) | The fact that the player is in the audience |
| [In Cinematic Fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/in_cinematic_fact) | If the player is in a cinematic |
| [Inventory Item Count Fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/inventory_item_count_fact) | The amount of a specific item in the player's inventory |
| [Item Holding Fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/item_holding_fact) | The amount of a specific item the player is currently holding |
| [Item In Slot Fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/item_in_slot_fact) | Check if a specific item is in a specific slot for the player |
| [Number Placeholder Fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/number_placeholder) | Computed Fact for a placeholder number |
| [Permanent Fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/permanent_fact) | Saved permanently, it never gets removed |
| [Quest Status Fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/quest_status_fact) | The status of a specific quest |
| [Session Fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/session_fact) | Saved until a player logouts of the server |
| [Timed Fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/timed_fact) | Saved for a specified duration, like 20 minutes |
| [Value Placeholder Fact](https://docs.typewritermc.com/adapters/BasicAdapter/entries/fact/value_placeholder) | Fact for a placeholder value |

### Groups {#groups}

| Name | Description |
| --- | --- |
| [Global Group](https://docs.typewritermc.com/adapters/BasicAdapter/entries/group/global_group) | One group with all the online players |
| [Player Group](https://docs.typewritermc.com/adapters/BasicAdapter/entries/group/player_group) | Group for every individual player |
| [World Group](https://docs.typewritermc.com/adapters/BasicAdapter/entries/group/world_group) | Group for the whole world |

### Quests {#quests}

| Name | Description |
| --- | --- |
| [Completable Objective](https://docs.typewritermc.com/adapters/BasicAdapter/entries/quest/completable_objective) | An objective that can show a completed stage |
| [Location Objective](https://docs.typewritermc.com/adapters/BasicAdapter/entries/quest/location_objective) | A location objective definition |
| [Objective Lines](https://docs.typewritermc.com/adapters/BasicAdapter/entries/quest/objective_lines) | Display all the current objectives |
| [Quest Complete Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/quest/quest_complete_event) | Triggered when a quest is completed for a player |
| [Quest Start Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/quest/quest_start_event) | Triggered when a quest is started for a player |
| [Quest Status Update Event](https://docs.typewritermc.com/adapters/BasicAdapter/entries/quest/quest_status_update_event) | Triggered when a quest status is updated for a player |
| [Simple Objective](https://docs.typewritermc.com/adapters/BasicAdapter/entries/quest/objective) | An objective definition |
| [Simple Quest](https://docs.typewritermc.com/adapters/BasicAdapter/entries/quest) | A quest definition |
| [Tracked Objective Audience](https://docs.typewritermc.com/adapters/BasicAdapter/entries/quest/tracked_objective_audience) | Filters an audience based on if they have a tracked objective |
| [Tracked Quest Audience](https://docs.typewritermc.com/adapters/BasicAdapter/entries/quest/tracked_quest_audience) | Filters an audience based on if they have a quest tracked |

### Sounds {#sounds}

| Name | Description |
| --- | --- |
| [Custom Sound](https://docs.typewritermc.com/adapters/BasicAdapter/entries/sound/custom_sound) | A custom sound |

### Statics {#statics}

| Name | Description |
| --- | --- |
| [Base Road Network](https://docs.typewritermc.com/adapters/BasicAdapter/entries/static/base_road_network) | A definition of the words road network |
| [Self Speaker](https://docs.typewritermc.com/adapters/BasicAdapter/entries/static/self_speaker) | The player themself |
| [Simple Speaker](https://docs.typewritermc.com/adapters/BasicAdapter/entries/static/simple_speaker) | The most basic speaker |
