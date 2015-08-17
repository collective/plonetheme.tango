/* This is a bundle that uses RequireJS to pull in dependencies.
   These dependencies are defined in the registry.xml file */


/* do not include jquery multiple times */
if(window.jQuery){
  define('jquery', [], function(){
    return window.jQuery;
  });
}

require([
  'jquery',
  'main',
  'pat-logger'
], function($, dep1, logger){
  'use strict';
  var log = logger.getLogger('requirejs');
  log.warn('loaded main value: ' + dep1);

  $(document).ready(function(){
    $('body').append('<p class="example-element">Added by example bundle</p>');
  });
});
