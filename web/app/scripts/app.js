'use strict';

/**
 * @ngdoc overview
 * @name teybApp
 * @description
 * # teybApp
 *
 * Main module of the application.
 */
angular
    .module('teybApp', ['ui.router', 'ngResource', 'ui.bootstrap', 'dialogs.main'])
    .run(
            [        '$rootScope', '$state', '$stateParams',
            function ($rootScope,   $state,   $stateParams) {

                // It's very handy to add references to $state and $stateParams to the $rootScope
                // so that you can access them from any scope within your applications.For example,
                // <li ui-sref-active="active }"> will set the <li> // to active whenever
                // 'contacts.list' or one of its decendents is active.
                $rootScope.$state = $state;
                $rootScope.$stateParams = $stateParams;
            }])
    .config(function($stateProvider, $urlRouterProvider, $httpProvider) {
            //
            // For any unmatched url, redirect to /state1
            $urlRouterProvider.otherwise("/about");
            //
            // Now set up the states
            $stateProvider
                        /*.state('home', {
                                url: "/home",
                                templateUrl: "views/main.html",
                                controller: "MainCtrl"
                        })*/
                        .state('quick_start', {
                                url: "/quickstart",
                                templateUrl: "views/quick_start.html",
                                controller: "QuickStartCtrl"
                        })
                        .state('tasks', {
                                url: "/tasks",
                                templateUrl: "views/tasks.html",
                                controller: "TasksCtrl"
                        })
                        .state('api_docs', {
                                url: "/api",
                                templateUrl: "views/api.html",
                                //controller: "TasksCtrl"
                        })
                        .state('about', {
                                url: "/about",
                                templateUrl: "views/about.html"
                        });

            // Setup Django CSRF protection.
            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        });
