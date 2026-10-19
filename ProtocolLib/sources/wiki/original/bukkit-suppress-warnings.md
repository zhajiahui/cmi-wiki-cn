By adding any of the following error or warning reports to *suppressed reports* in *config.yml*, they will no longer be printed to the console.
Example:

```
global:
  auto updater:
    notify: true
    download: false
    delay: 43200
  metrics: true
  background compiler: true
  suppressed reports:
  - REPORT_DETECTED_CUSTOM_SERVER_HANDLER
```

|  |  |
| --- | --- |
| Report Name | Text |
| REPORT\_EXCEPTION\_COUNT | Internal exception count: %s! |
| REPORT\_CANNOT\_SEND\_MESSAGE | Cannot send chat message. |
| REPORT\_COMMAND\_ERROR | Cannot execute command %s. |
| REPORT\_UNEXPECTED\_COMMAND | Incorrect command assigned to %s. |
| REPORT\_FALLBACK\_ENGINE | Falling back to the Rhino engine. |
| REPORT\_CANNOT\_LOAD\_FALLBACK\_ENGINE | Could not load Rhino either. Please upgrade your JVM or OS. |
| REPORT\_PACKAGES\_UNSUPPORTED\_IN\_ENGINE | Unable to initialize packages for JavaScript engine. |
| REPORT\_FILTER\_REMOVED\_FOR\_ERROR | Removing filter %s for causing %s. |
| REPORT\_CANNOT\_HANDLE\_CONVERSATION | Cannot handle conversation. |
| REPORT\_ILLEGAL\_ARGUMENT | Illegal argument. |
| REPORT\_SECURITY\_LIMITATION | Security limitation. |
| REPORT\_CANNOT\_FIND\_UNWRAP\_METHOD | Cannot find method. |
| REPORT\_CANNOT\_READ\_FIELD\_HANDLE | Cannot read field 'handle'. |
| REPORT\_CANNOT\_LOAD\_PACKET\_LIST | Cannot load server and client packet list. |
| REPORT\_CANNOT\_INITIALIZE\_PACKET\_INJECTOR | Unable to initialize packet injector |
| REPORT\_PLUGIN\_DEPEND\_MISSING | %s doesn't depend on ProtocolLib. Check that its plugin.yml has a 'depend' directive. |
| REPORT\_UNSUPPORTED\_SERVER\_PACKET\_ID | [%s] Unsupported server packet ID in current Minecraft version: %s |
| REPORT\_UNSUPPORTED\_CLIENT\_PACKET\_ID | [%s] Unsupported client packet ID in current Minecraft version: %s |
| REPORT\_CANNOT\_UNINJECT\_PLAYER | Unable to uninject net handler for player. |
| REPORT\_CANNOT\_UNINJECT\_OFFLINE\_PLAYER | Unable to uninject logged off player. |
| REPORT\_CANNOT\_INJECT\_PLAYER | Unable to inject player. |
| REPORT\_CANNOT\_UNREGISTER\_PLUGIN | Unable to handle disabled plugin. |
| REPORT\_HTTP\_ERROR | Http error: %s |
| REPORT\_CANNOT\_CHECK\_FOR\_UPDATES | Cannot check updates for ProtocolLib. |
| REPORT\_CANNOT\_UPDATE\_PLUGIN | Cannot update ProtocolLib. |
| REPORT\_TOO\_MANY\_GENERATED\_CLASSES | Generated too many classes (count: %s) |
| REPORT\_ASSUME\_DISCONNECT\_METHOD | Cannot find disconnect method by name. Assuming %s. |
| REPORT\_INVALID\_ARGUMENT\_DISCONNECT | Invalid argument passed to disconnect method: %s |
| REPORT\_CANNOT\_ACCESS\_DISCONNECT | Unable to access disconnect method. |
| REPORT\_CANNOT\_CLOSE\_SOCKET | Unable to close socket. |
| REPORT\_ACCESS\_DENIED\_CLOSE\_SOCKET | Insufficient permissions. Cannot close socket. |
| REPORT\_DETECTED\_CUSTOM\_SERVER\_HANDLER | Detected server handler proxy type by another plugin. Conflict may occur! |
| REPORT\_CANNOT\_PROXY\_SERVER\_HANDLER | Unable to load server handler from proxy type. |
| REPORT\_CANNOT\_UPDATE\_PLAYER | Cannot update player in PlayerEvent. |
| REPORT\_CANNOT\_HANDLE\_PACKET | Cannot handle server packet. |
| REPORT\_ASSUMING\_DISCONNECT\_FIELD | Unable to find 'disconnected' field. Assuming %s. |
| REPORT\_DISCONNECT\_FIELD\_MISSING | Cannot find disconnected field. Is ProtocolLib up to date? |
| REPORT\_DISCONNECT\_FIELD\_FAILURE | Unable to update disconnected field. Player quit event may be sent twice. |
| REPORT\_CANNOT\_HANDLE\_CLIENT\_PACKET | Cannot handle client packet. |
| REPORT\_CANNOT\_FIND\_MINECRAFT\_SERVER | Cannot extract minecraft server from Bukkit. |
| REPORT\_CANNOT\_INJECT\_SERVER\_CONNECTION | Cannot inject into server connection. Bad things will happen. |
| REPORT\_CANNOT\_FIND\_LISTENER\_THREAD | Cannot find listener thread in MinecraftServer. |
| REPORT\_CANNOT\_READ\_LISTENER\_THREAD | Unable to read the listener thread. |
| REPORT\_CANNOT\_FIND\_SERVER\_CONNECTION | Unable to retrieve server connection |
| REPORT\_UNEXPECTED\_THREAD\_COUNT | Unexpected number of threads in %s: %s |
| REPORT\_CANNOT\_FIND\_NET\_HANDLER\_THREAD | Unable to retrieve net handler thread. |
| REPORT\_INSUFFICENT\_THREAD\_COUNT | Unable to inject %s lists in %s. |
| REPORT\_CANNOT\_COPY\_OLD\_TO\_NEW | Cannot copy old %s to new. |
| REPORT\_CANNOT\_CORRECT\_TROVE\_MAP | Unable to correct no entry value. |
| REPORT\_INSUFFICIENT\_SERVER\_PACKETS | Too few server packets detected: %s |
| REPORT\_INSUFFICIENT\_CLIENT\_PACKETS | Too few client packets detected: %s |
| REPORT\_UNSUPPPORTED\_LISTENER | Cannot fully register listener for %s: %s |
| REPORT\_PLAYER\_HOOK\_FAILED | Player hook %s failed. |
| REPORT\_SWITCHED\_PLAYER\_HOOK | Switching to %s instead. |
| REPORT\_HOOK\_CLEANUP\_FAILED | Cleaing up after player hook failed. |
| REPORT\_CANNOT\_REVERT\_HOOK | Unable to fully revert old injector. May cause conflicts. |
| REPORT\_CANNOT\_HOOK\_LOGIN\_HANDLER | Unable to hook %s. |
| REPORT\_CANNOT\_CLEANUP\_LOGIN\_HANDLER | Cannot cleanup %s. |
| REPORT\_CANNOT\_RESET\_FIELD | Unable to reset field %s: %s |
| REPORT\_CANNOT\_UNLOAD\_CLASS | Unable to unload class %s. |
| REPORT\_CANNOT\_COMPILE\_STRUCTURE\_MODIFIER | Cannot compile structure. Disabing compiler. |
| REPORT\_CANNOT\_SCHEDULE\_COMPILATION | Unable to schedule compilation task. |
| REPORT\_CANNOT\_FIND\_READ\_PACKET\_METHOD | Cannot find read packet method for ID %s. |
| REPORT\_UNKNOWN\_ORIGIN\_FOR\_PACKET | Timeout: Unknown origin %s for packet %s. Are you using GamePhase.LOGIN? |

Please report problems and error messages as a ticket [here](http://dev.bukkit.org/bukkit-plugins/protocollib/tickets).
