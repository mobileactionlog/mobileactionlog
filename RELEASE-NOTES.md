# Release-Notes for v4.1.0

--- Preliminary release notes ---

## Mobile ActionLog Android App

* Support for *two* new hardware devices: CAT S52, Samsung Galaxy XCover Pro.
* Support for logging actions with full GNSS data: latitude, longitude, altitude.
* Support for a static grid with grid bearing and latitude/longitude/altitude for grid origin.
* Connection to an AIS transponder is no longer required when not in AIS-Grid mode.
* Basic Authentication to secure the connection to the SyncServer.
* Logging actions is possible without any configured grid.
* A new screen that shows the current app and grid configuration.
* Filtering and Sorting in the list views for logistical installations, device operations, and waypoints.

## SyncServer

* Export device operations as JSON with full GNSS data
* Configuration of two modes: AIS-Grid with transponder, or STATIC-Grid with only the tablet
* Basic Authentication to secure the connection to the Android App and the SyncServer UI.
* New administration SyncServer UI to support displaying device installations/operations and logistical installations.

# Known issues
  
## Mobile ActionLog App

* Connection to the AIS transponder is sometimes kept alive if the App was switched from AIS to STATIC grid.
  Restarting the app fixes the issue.
  
* The grid is not keeping the position if zooming in with the `+`-button. This is due to a limitation in the
  underlying 3rd-party drawing library.
  
## SyncServer

* A _whitelabel_ default error page is shown instead of
  proper error pages when i.e. a resource is not found (http error 404).
  

    