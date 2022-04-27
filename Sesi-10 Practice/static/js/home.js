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
        // TYPE
        'read_type': function() {
            let ajax_options = {
                type: 'GET',
                url: 'api/type',
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
                .done(function(data) {
                    $event_pump.trigger('model_read_success_type', [data]);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                })
        },
        create_type: function(type) {
            let ajax_options = {
                type: 'POST',
                url: 'api/type',
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'type': type
                }),
            };
            $.ajax(ajax_options)
                .done(function(data) {
                    $event_pump.trigger('model_create_success_type', [data]);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                })
        },
        update_type: function(typeid, type) {
            let ajax_options = {
                type: 'PUT',
                url: 'api/type/' + parseInt(typeid),
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'type': type,
                })
            };
            $.ajax(ajax_options)
                .done(function(data) {
                    $event_pump.trigger('model_update_success_type', [data]);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                })
        },
        'delete_type': function(typeid) {
            let ajax_options = {
                type: 'DELETE',
                url: 'api/type/' + parseInt(typeid),
                accepts: 'application/json',
                contentType: 'plain/text'
            };
            $.ajax(ajax_options)
                .done(function(data) {
                    $event_pump.trigger('model_delete_success_type', [data]);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                })
        },
        // REGION
        'read_region': function() {
            let ajax_options = {
                type: 'GET',
                url: 'api/region',
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
                .done(function(data) {
                    $event_pump.trigger('model_read_success_region', [data]);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                })
        },
        create_region: function(region) {
            let ajax_options = {
                type: 'POST',
                url: 'api/region',
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'region': region
                }),
            };
            $.ajax(ajax_options)
                .done(function(data) {
                    $event_pump.trigger('model_create_success_region', [data]);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                })
        },
        update_region: function(regionid, region) {
            let ajax_options = {
                type: 'PUT',
                url: 'api/region/' + parseInt(regionid),
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'region': region,
                })
            };
            $.ajax(ajax_options)
                .done(function(data) {
                    $event_pump.trigger('model_update_success_region', [data]);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                })
        },
        'delete_region': function(regionid) {
            let ajax_options = {
                type: 'DELETE',
                url: 'api/region/' + parseInt(regionid),
                accepts: 'application/json',
                contentType: 'plain/text'
            };
            $.ajax(ajax_options)
                .done(function(data) {
                    $event_pump.trigger('model_delete_success_region', [data]);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                })
        },
        // AVOCADO
        'read_avo': function() {
            let ajax_options = {
                type: 'GET',
                url: 'api/avocado',
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
                .done(function(data) {
                    $event_pump.trigger('model_read_success', [data]);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                })
        },
        create_avo: function(avgprice, totalvol, avo_a, avo_b, avo_c, avo_type, avo_region) {
            let ajax_options = {
                type: 'POST',
                url: 'api/avocado',
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'avgprice': parseFloat(avgprice),
                    'totalvol': parseFloat(totalvol),
                    'avo_a': parseInt(avo_a),
                    'avo_b': parseFloat(avo_b),
                    'avo_c': parseFloat(avo_c),
                    'type': parseInt(avo_type),
                    'regionid': parseInt(avo_region)
                }),
            };
            $.ajax(ajax_options)
                .done(function(data) {
                    $event_pump.trigger('model_create_success', [data]);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                })
        },
        update_avo: function(avocadoid, avgprice, totalvol, avo_a, avo_b, avo_c, avo_type, avo_region) {
            let ajax_options = {
                type: 'PUT',
                url: 'api/avocado/' + avocadoid,
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'avgprice': parseFloat(avgprice),
                    'totalvol': parseFloat(totalvol),
                    'avo_a': parseInt(avo_a),
                    'avo_b': parseFloat(avo_b),
                    'avo_c': parseFloat(avo_c),
                    'type': parseInt(avo_type),
                    'regionid': parseInt(avo_region)
                })
            };
            $.ajax(ajax_options)
                .done(function(data) {
                    $event_pump.trigger('model_update_success', [data]);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                })
        },
        'delete_avo': function(avocadoid) {
            let ajax_options = {
                type: 'DELETE',
                url: 'api/avocado/' + parseInt(avocadoid),
                accepts: 'application/json',
                contentType: 'plain/text'
            };
            $.ajax(ajax_options)
                .done(function(data) {
                    $event_pump.trigger('model_delete_success', [data]);
                })
                .fail(function(xhr, textStatus, errorThrown) {
                    $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
                })
        }
    };
}());

// Create the view instance
ns.view = (function() {
    'use strict';

    let $avocadoid = $('#avocadoid'),
        $avgprice = $('#avgprice'),
        $totalvol = $('#totalvol'),
        $avo_a = $('#avo_a'),
        $avo_b = $('#avo_b'),
        $avo_c = $('#avo_c'),
        $avo_type = $('#avo_type'),
        $avo_region = $('#avo_region'),
        $typeid = $('#typeid'),
        $type = $('#type'),
        $regionid = $('#regionid'),
        $region = $('#region');

    // return the API
    return {
        reset: function() {
            $avocadoid.val('');
            $avgprice.val('');
            $totalvol.val('');
            $avo_a.val('');
            $avo_b.val('');
            $avo_c.val('');
            $avo_type.val('');
            $avo_region.val('');
            $typeid.val('');
            $type.val('');
            $regionid.val('');
            $region.val('');
        },
        update_editor: function(avocadoid, avgprice, totalvol, avo_a, avo_b, avo_c, avo_type, avo_region) {
            $avocadoid.val(avocadoid).focus();
            $avgprice.val(avgprice);
            $totalvol.val(totalvol);
            $avo_a.val(avo_a);
            $avo_b.val(avo_b);
            $avo_c.val(avo_c);
            $avo_type.val(avo_type);
            $avo_region.val(avo_region);
        },
        build_table: function(avocado) {
            let rows = ''

            // clear the table
            $('.avocado table > tbody').empty();

            // did we get a avocado array?
            if (avocado) {
                for (let i = 0, l = avocado.length; i < l; i++) {
                    rows += `<tr>
                                <td hidden class="avocadoid">${avocado[i].avocadoid}</td>
                                <td class="avgprice">${avocado[i].avgprice}</td>
                                <td class="totalvol">${avocado[i].totalvol}</td>
                                <td class="avo_a">${avocado[i].avo_a}</td>
                                <td class="avo_b">${avocado[i].avo_b}</td>
                                <td class="avo_c">${avocado[i].avo_c}</td>
                                <td class="avo_type">${avocado[i].type}</td>
                                <td class="avo_region">${avocado[i].regionid}</td>
                                <td>${avocado[i].date}</td>
                            </tr>`;
                }
                $('table.table_avo > tbody').append(rows);
            }
        },
        build_table_type: function(type) {
            let rows = ''

            // clear the table
            $('.type_table table > tbody').empty();

            // did we get a avocado array?
            if (type) {
                for (let i = 0, l = type.length; i < l; i++) {
                    rows += `<tr>
                                <td>${type[i].typeid}</td>
                                <td>${type[i].type}</td>
                            </tr>`;
                }
                $('table.table_type > tbody').append(rows);
            }
        },
        build_table_region: function(region) {
            let rows = ''

            // clear the table
            $('.region_table table > tbody').empty();

            // did we get a avocado array?
            if (region) {
                for (let i = 0, l = region.length; i < l; i++) {
                    rows += `<tr>
                                <td>${region[i].regionid}</td>
                                <td>${region[i].region}</td>
                            </tr>`;
                }
                $('table.table_region > tbody').append(rows);
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
        $event_pump = $('body'),
        $avocadoid = $('#avocadoid'),
        $type = $('#type'),
        $typeid = $('#typeid'),
        $region = $('#region'),
        $regionid = $('#regionid'),
        $avgprice = $('#avgprice'),
        $totalvol = $('#totalvol'),
        $avo_a = $('#avo_a'),
        $avo_b = $('#avo_b'),
        $avo_c = $('#avo_c'),
        $avo_type = $('#avo_type'),
        $avo_region = $('#avo_region');

    // Get the data from the model after the controller is done initializing
    setTimeout(function() {
        model.read_avo();
        model.read_type();
        model.read_region();
    }, 100)

    // Validate input
    function validate(avgprice, totalvol, avo_a, avo_b, avo_c, avo_type, avo_region) {
        return (avgprice >= 0 &&
            totalvol >= 0 && avo_a >= 0 &&
            avo_b >= 0 && avo_c >= 0 &&
            avo_type >= 0 && avo_region >= 0
        );
    }

    // Create our event handlers
    // TYPE
    $('#create_type').click(function(e) {
        let type = $type.val()
        e.preventDefault();

        model.create_type(type);
        e.preventDefault();
    });

    $('#update_type').click(function(e) {
        let typeid = $typeid.val(),
            type = $type.val();
        e.preventDefault();

        model.update_type(typeid, type);
        e.preventDefault();
    });

    $('#delete_type').click(function(e) {
        let typeid = $typeid.val();
        e.preventDefault();

        model.delete_type(typeid)
        e.preventDefault();
    });
    // REGION
    $('#create_region').click(function(e) {
        let region = $region.val()
        e.preventDefault();

        model.create_region(region)
        e.preventDefault();
    });

    $('#update_region').click(function(e) {
        let regionid = $regionid.val(),
            region = $region.val();
        e.preventDefault();

        model.update_region(regionid, region);
        e.preventDefault();
    });

    $('#delete_region').click(function(e) {
        let regionid = $regionid.val();
        e.preventDefault();

        model.delete_region(regionid);
        e.preventDefault();
    });
    // AVOCADO
    $('#create_avo').click(function(e) {
        let avgprice = $avgprice.val(),
            totalvol = $totalvol.val(),
            avo_a = $avo_a.val(),
            avo_b = $avo_b.val(),
            avo_c = $avo_c.val(),
            avo_type = $avo_type.val(),
            avo_region = $avo_region.val();

        e.preventDefault();

        if (validate(avgprice, totalvol, avo_a, avo_b, avo_c, avo_type, avo_region)) {
            model.create_avo(avgprice, totalvol, avo_a, avo_b, avo_c, avo_type, avo_region)
        } else {
            alert('Problem with input');
        }
    });

    $('#update_avo').click(function(e) {
        let avocadoid = $avocadoid.val(),
            avgprice = $avgprice.val(),
            totalvol = $totalvol.val(),
            avo_a = $avo_a.val(),
            avo_b = $avo_b.val(),
            avo_c = $avo_c.val(),
            avo_type = $avo_type.val(),
            avo_region = $avo_region.val();

        e.preventDefault();

        if (validate(avgprice, totalvol, avo_a, avo_b, avo_c, avo_type, avo_region)) {
            model.update_avo(avocadoid, avgprice, totalvol, avo_a, avo_b, avo_c, avo_type, avo_region)
        } else {
            alert('Problem with input');
        }
        e.preventDefault();
    });

    $('#delete_avo').click(function(e) {
        let avocadoid = $avocadoid.val();
        e.preventDefault();

        model.delete_avo(avocadoid);
        e.preventDefault();
    });

    $('#reset').click(function() {
        view.reset();
    })

    $('table.table_avo > tbody').on('dblclick', 'tr', function(e) {
        let $target = $(e.target),
            avocadoid, avgprice, totalvol,
            avo_a, avo_b, avo_c, avo_type, avo_region;

        avocadoid = $target
            .parent()
            .find('td.avocadoid')
            .text();

        avgprice = $target
            .parent()
            .find('td.avgprice')
            .text();

        totalvol = $target
            .parent()
            .find('td.totalvol')
            .text();

        avo_a = $target
            .parent()
            .find('td.avo_a')
            .text();

        avo_b = $target
            .parent()
            .find('td.avo_b')
            .text();

        avo_c = $target
            .parent()
            .find('td.avo_c')
            .text();

        avo_type = $target
            .parent()
            .find('td.avo_type')
            .text();

        avo_region = $target
            .parent()
            .find('td.avo_region')
            .text();

        view.update_editor(avocadoid, avgprice, totalvol, avo_a, avo_b, avo_c, avo_type, avo_region);
    });

    // Handle the model events TYPE
    $event_pump.on('model_read_success_type', function(e, data) {
        view.build_table_type(data);
        view.reset();
    });

    $event_pump.on('model_create_success_type', function(e, data) {
        model.read_type();
        alert('Success add new type');
    });

    $event_pump.on('model_update_success_type', function(e, data) {
        model.read_type();
        alert('Success update type');
    });

    $event_pump.on('model_delete_success_type', function(e, data) {
        model.read_type();
        alert('Success delete type');
    });

    // Handle the model events REGION
    $event_pump.on('model_read_success_region', function(e, data) {
        view.build_table_region(data);
        view.reset();
    });

    $event_pump.on('model_create_success_region', function(e, data) {
        model.read_region();
        alert('Success add new region');
    });

    $event_pump.on('model_update_success_region', function(e, data) {
        model.read_region();
        alert('Success update region');
    });

    $event_pump.on('model_delete_success_region', function(e, data) {
        model.read_region();
        alert('Success delete region');
    });

    // Handle the model events AVOCADO
    $event_pump.on('model_read_success', function(e, data) {
        view.build_table(data);
        view.reset();
    });

    $event_pump.on('model_create_success', function(e, data) {
        model.read_avo();
        alert('Success add new data');
    });

    $event_pump.on('model_update_success', function(e, data) {
        model.read_avo();
        alert('Success update data');
    });

    $event_pump.on('model_delete_success', function(e, data) {
        model.read_avo();
        alert('Success delete data');
    });

    $event_pump.on('model_error', function(e, xhr, textStatus, errorThrown) {
        let error_msg = textStatus + ': ' + errorThrown + ' - ' + xhr.responseJSON.detail;
        view.error(error_msg);
        console.log(error_msg);
    })
}(ns.model, ns.view));