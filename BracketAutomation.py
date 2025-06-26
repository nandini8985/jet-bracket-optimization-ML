import adsk.core, adsk.fusion, traceback

def run(context):
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = app.activeProduct
        userParams = design.userParameters
        timeline = design.timeline
        doc = app.activeDocument

        exportMgr = design.exportManager

        # Values to test
        hole_diams = [18, 20, 22]
        rib_thicknesses = [16, 18, 20]
        fillets = [3, 5, 7]

        # Export folder path (change this if needed)
        folder_path = 'C:/Users/DELL/Downloads/FusionExports'

        # Loop through combinations
        for h in hole_diams:
            for r in rib_thicknesses:
                for f in fillets:
                    # Set user parameters
                    userParams.itemByName('top_hole_dia').expression = f'{h} mm'
                    userParams.itemByName('bottom_hole_dia').expression = f'{h / 2} mm'
                    userParams.itemByName('rib_thickness').expression = f'{r} mm'
                    userParams.itemByName('fillet_r').expression = f'{f} mm'

                    # Regenerate model
                    timeline.moveToEnd()

                    # Create a unique file name
                    file_name = f'Bracket_h{h}_r{r}_f{f}'

                    # Create STEP export options
                    step_options = exportMgr.createSTEPExportOptions(f'{folder_path}/{file_name}.step')
                    exportMgr.execute(step_options)

                    # Optional: Export STL as well
                    # stl_options = exportMgr.createSTLExportOptions(design.rootComponent, f'{folder_path}/{file_name}.stl')
                    # exportMgr.execute(stl_options)

                    # Confirmation message
                    ui.messageBox(f'Exported: {file_name}.step')

    except:
        if ui:
            ui.messageBox('Script failed:\n{}'.format(traceback.format_exc()))


