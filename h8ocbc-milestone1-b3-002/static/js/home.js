/*
 * JavaScript file for the application to demonstrate
 * using the API
 */

// Create the namespace instance
let ns = {};

// Create the model instance
ns.model = (function() {
    'use strict';

    let $event_pump = $('body');

    // Return the API
    return {
        'read_movie': function() {
            let ajax_options = {
                type: 'GET',
                url: 'api/movie',
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
                .done(function(data) {
                    $event_pump.trigger('model_read_success_movie', [data]);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                })
        },
        'read_director': function() {
            let ajax_options = {
                type: 'GET',
                url: 'api/director',
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
                .done(function(data) {
                    $event_pump.trigger('model_read_success_director', [data]);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                })
        },
    };
}());

// Create the view instance
ns.view = (function() {
    'use strict';
    // return the API
    return {
        build_table_movie: function(movie) {
            let rows = ''

            // clear the table
            $('.movie table > tbody').empty();

            if (movie) {
                for (let i = 0, l = 10; i < l; i++) {
                    rows += `<tr>
                                <td>${movie[i].title}</td>
                                <td>${movie[i].release_date}</td>
                                <td>${movie[i].budget}</td>
                                <td>${movie[i].revenue}</td>
                                <td>${movie[i].popularity}</td>
                                <td>${movie[i].director_id}</td>
                            </tr>`;
                }
                $('table.table_movie > tbody').append(rows);
            }
        },
        build_table_director: function(director) {
            let rows = ''

            // clear the table
            $('.director table > tbody').empty();

            if (director) {
                for (let i = 0, l = 10; i < l; i++) {
                    rows += `<tr>
                                <td>${director[i].id}</td>
                                <td>${director[i].name}</td>
                                <td>${director[i].gender}</td>
                                <td>${director[i].department}</td>
                            </tr>`;
                }
                $('table.table_director > tbody').append(rows);
            }
        },
        error: function(error_msg) {
            $('.error')
                .text(error_msg)
                .css('visibility', 'visible');
            setTimeout(function() {
                $('.error').css('visibility', 'hidden');
            }, 3000)
        }
    };
}());

// Create the controller
ns.controller = (function(m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body');

    // Get the data from the model after the controller is done initializing
    setTimeout(function() {
        model.read_movie();
        model.read_director();
    }, 100)

    // Handle the model events TYPE
    $event_pump.on('model_read_success_movie', function(e, data) {
        view.build_table_movie(data);
    });
    $event_pump.on('model_read_success_director', function(e, data) {
        view.build_table_director(data);
    });
    $event_pump.on('model_error', function(e, xhr, textStatus, errorThrown) {
        let error_msg = textStatus + ': ' + errorThrown + ' - ' + xhr.responseJSON.detail;
        view.error(error_msg);
        console.log(error_msg);
    })

}(ns.model, ns.view));