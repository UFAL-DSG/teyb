'use strict';


angular.module('teybApp')
    .factory('Tasks', function($resource){
        return $resource('/api/tasks', {})
    })
    .factory('registerTeam', function($window, $http, $q) {
        var msgs = [];

        return function(email, name) {
            var data = {
                email: email,
                name: name,
            };

            var deferred = $q.defer();

            $http.post("/register", data)
                .success(function(data) {
                    deferred.resolve(data);
                })
                .error(function(data) {
                    deferred.reject(data);
                });
            return deferred.promise;
        };
    });